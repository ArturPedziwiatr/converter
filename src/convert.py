import sys
import os
import subprocess
import re
import laspy
import zipfile

from typing import Union
from fastapi import File
from src.logger import console

class Converter:
    @staticmethod
    def tupleToStr(tup):
        st = ''.join(map(str, tup))
        return st

    @staticmethod
    def lazToLas(path: str) -> str:
        console.log("Start converting .laz file to .las")
        fileName = os.path.basename(path).split('.')[0]
        file = laspy.read(path)
        file = laspy.convert(file)
        print(fileName)
        output = './src/tmp/{}.las'.format(fileName)
        file.write(output)
        console.log("Finished converting")
        return output

    @staticmethod
    def lasTo3DTiles(input: str, output: str, epsg: str) -> str:
        console.log("Start converting .laz file to 3DTiles")
        try:    
            subprocess.run(
                [
                    './src/gocesiumtiler',
                    '-i', input,
                    '-o', output,
                    '-e', epsg
                ],
                check=True
            )
            return '{}/{}'.format(output,os.path.basename(input).split('.')[0])
        except subprocess.CalledProcessError as e:
            console.error(f"Error with gocesiumtiler: {e}")
        console.log("Finished converting")


class DataExtractor:
    @staticmethod
    def getEPSG(input: str) -> str:
        console.log("Get EPSG from file")
        epsg: str
        try:
            epsg = re.search(
                r'(?<=EPSG:)\d+',
                Converter.tupleToStr(
                    subprocess.Popen(['entwine', 'info', input], stdout=subprocess.PIPE).communicate()
                )
            ).group()
            console.log("EPSG: {} has been download".format(epsg))
            return epsg
        except  subprocess.CalledProcessError as e:
            console.error("Error with entwine: {}".format(e))
