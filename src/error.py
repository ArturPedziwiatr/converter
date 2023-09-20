from src.logger import console
from enum import Enum

class Error(Enum):
  WrongEpsgError='001'
  NotDefinde='002'
  WrongExtension='003'

class Throw(Exception):
  def __init__(self, context= '',  msg='', name='Unknown error', code='unknown'):
    console.error('[{}] | {}'.format(context, msg))
    self.msg = msg
    self.name = name
    self.code = code
    super().__init__(msg, context, name, code)

class WrongEpsg(Throw):
  def __init__(self, context, msg='Error with download EPSG'): 
    super().__init__(
      context,
      msg,
      Error.WrongEpsgError.name,
      Error.WrongEpsgError.value
    )

class NotDefined(Throw):
  def __init__(self, context, msg='Element is not defined'): 
    super().__init__(
      context,
      msg,
      Error.NotDefinde.name,
      Error.NotDefinde.value
    )

class WrongExtension(Throw):
  def __init__(self, context, msg='Unknown extension'): 
    super().__init__(
      context,
      msg,
      Error.WrongExtension.name,
      Error.WrongExtension.value
    )
