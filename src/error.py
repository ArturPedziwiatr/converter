from src.logger import console
from enum import Enum

class Error(Enum):
  goCesiumTiler = { 
    'name': 'Error with gocesiumtiler',
    'code': '001'
  }
  pdal = { 
    'name': 'Error with pdal',
    'code': '002'
  }
  wrongEpsg = { 
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
      *err,
      msg
    }
    super().__init__(error)
