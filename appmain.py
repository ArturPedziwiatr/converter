import os
import uuid

from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse, StreamingResponse
from src.convert import Converter, DataExtractor
from src.logger import console
from src.error import NotDefined, Throw, WrongExtension

app = FastAPI()
tmpPath = './src/tmp'
outputPath = 'output'

@app.get("/")
async def hello():
    return {
        "Servis": "working properly",
        "active": True
    }
    

@app.post("/v1/laz-to-tiles")
async def lazToTiles(
    file: UploadFile,
    filename: str = Form(...),
    mimeType: str = Form(...)
):
    try:
        uuid4 = uuid.uuid4()
        if not os.path.exists(tmpPath):
            os.mkdir(tmpPath)

        if type( filename ) is not str:
            raise NotDefined('lazToTiles', 'Name of file is not')
        if (filename.find('.laz') < 0 & filename.find('.las') < 0):
            raise WrongExtension('lazToTiles', 'Expected file with (.laz|.las) extension')


        filePath = '{}/{}.{}'.format(tmpPath, uuid4, filename.split('.')[-1])
        with open(filePath, '+wb') as f:
            f.write(await file.read())

        
        if filename.find('.laz') > -1:
            filePath = Converter.lazToLas(filePath, True)

        epsg = DataExtractor.getEPSG(filePath)
        Converter.lasTo3DTiles(filePath, outputPath, epsg, True)

        return uuid4
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