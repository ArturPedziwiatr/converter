import os
import subprocess
import re
import laspy
import json
from src.logger import console
from src.error import Throw, Error

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
        subprocess.run(
            [
                './src/gocesiumtiler',
                '-i', input,
                '-o', output,
                '-e', epsg
            ],
            check=True
        )
        console.log("Finished converting")
        return '{}/{}'.format(output,os.path.basename(input).split('.')[0])


class DataExtractor:
    @staticmethod
    def getEPSG(input: str) -> str:
        console.log("Get EPSG from file")
        epsgLoader = json.loads(
            subprocess.run(
                ['pdal', 'info', input, '--summary'],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            ).stdout
        )['summary']['metadata']['srs']['wkt']
        if not epsgLoader:
            Throw(Error.wrongEpsg, 'Cannot find EPSG', 'getEPSG')
        matches = list(re.finditer(
            r'(?<=EPSG.{3})\d+',
            epsgLoader
        ))
        if matches:
            epsg = matches[-1].group()
        if not epsg:
            Throw(Error.wrongEpsg, 'Cannot find EPSG', 'getEPSG')
        return epsg


