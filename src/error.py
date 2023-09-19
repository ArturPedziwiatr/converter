from src.logger import console
from enum import Enum

class Error(Enum):
  def goCesiumTiler():
    return { 
      'name': 'Error with gocesiumtiler',
      'code': '001'
    }
  def pdal():
    return{ 
      'name': 'Error with pdal',
      'code': '002'
    }
  def wrongEpsg():
    return { 
      'name': 'Error with download EPSG',
      'code': '003'
    }
  def notDefined(lab: str):
    return {
      'name': '{} is not defined'.format(lab),
      'code': '004'
    }

class Throw(Exception):
  def __init__(self, err: Error, msg: any, context: str):
    if not msg:
      msg = err.name
    console.error('[{}] | {}'.format(context, msg))
    error = {
      'name': err['name'],
      'code': err['code'],
      'msg': msg
    }
    super().__init__(error)
