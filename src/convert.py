import os
import subprocess
import re
import laspy
import shutil
import json
from src.logger import console
from src.error import Throw, WrongEpsg

class Converter:
    @staticmethod
    def tupleToStr(tup):
        st = ''.join(map(str, tup))
        return st
    
    @staticmethod
    def dirToZip(path: str, rm:bool = False) -> str:
        console.log("Start compressing to zip")
        shutil.make_archive(
            path,
            'zip',
            path
        )
        if rm & os.path.exists(path):
            shutil.rmtree(path)
        console.log("Compressing has been finished")
        return '{}.zip'.format(path)

    @staticmethod
    def lazToLas(path: str, rm: bool = False) -> str:
        console.log("Start converting .laz file to .las")
        file = laspy.read(path)
        file = laspy.convert(file)
        output = '{}.las'.format(os.path.splitext(path)[0])
        file.write(output)
        if rm & os.path.exists(path):
            os.remove(path)
        console.log("Finished converting")
        return output

    @staticmethod
    def lasTo3DTiles(input: str, output: str, epsg: str, rm:bool = False) -> str:
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
        if rm & os.path.exists(input):
            os.remove(input)
        console.log("Finished converting")
        return os.path.splitext(input)[0]

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
            raise WrongEpsg('getEPSG')
        matches = list(re.finditer(
            r'(?<=EPSG.{3})\d+',
            epsgLoader
        ))
        if matches:
            epsg = matches[-1].group()
        if not epsg:
            raise WrongEpsg('getEPSG')
        return epsg


