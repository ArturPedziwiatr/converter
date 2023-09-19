import os
import re
import subprocess
import shutil

from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from src.convert import Converter, DataExtractor
from src.logger import console
from src.error import NotDefined, Throw

app = FastAPI()
tmpPath = './src/tmp'

@app.get("/")
async def hello():
    return {"hello": "world"}

@app.post("/v1/laz-to-tiles")
async def lazToTiles(file: UploadFile):
    try:
        if os.path.exists(tmpPath):
            shutil.rmtree(tmpPath)
        os.mkdir(tmpPath)
        filename = file.filename
        if type( filename ) is not str:
            raise NotDefined('lazToTiles', 'Name of file is not')

        filePath = '{}/{}'.format(tmpPath,filename)
        with open(filePath, '+wb') as f:
            f.write(await file.read())
        
        if filename.find('.laz') > -1:
            filePath = Converter.lazToLas(filePath)

        epsg = DataExtractor.getEPSG(filePath)
        folderResult = Converter.lasTo3DTiles(filePath, tmpPath, epsg)
        if os.path.exists(filePath):
            os.remove(filePath)

        fileZip =  '{}/{}'.format(tmpPath, filename.split('.')[0])
        shutil.make_archive(
            fileZip,
            'zip',
            folderResult
        )

        if os.path.exists(folderResult):
            shutil.rmtree(folderResult)


        return FileResponse('{}.zip'.format(fileZip))
    except Throw as err:
        return JSONResponse(content={
            'name': err.name,
            'code': err.code,
            'msg': err.msg
        })
    except Exception as e:
        console.error('An error occurred: {}'.format(e))
        return JSONResponse(content={
            'name': 'unknown',
            'code': 'unknown',
            'msg': e
        })