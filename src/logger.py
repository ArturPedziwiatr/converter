import os
import datetime

class color:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

class style:
  BOLD = '\033[1m'
  END = '\033[0m'


class console:
  def __writeToFile(msg: str):
    if not ( os.path.exists('./log') ):
      os.mkdir('./log')
    file = open('./log/log.txt', '+a')
    file.write('{} \n'.format(msg))
    file.close()
  
  @staticmethod
  def log(msg: str):
    message = '( LOG )   [{}] --- {}'.format(datetime.datetime.now(), msg)
    print(color.GREEN + message + style.END)
    console.__writeToFile(message)

  @staticmethod
  def info(msg: str):
    message = '( INFO )  [{}] --- {}'.format(datetime.datetime.now(), msg)
    print(color.BLUE + message + style.END)
    console.__writeToFile(message)

  @staticmethod
  def error(msg: str):
    message = '( ERROR ) [{}] --- {}'.format(datetime.datetime.now(), msg)
    print(color.RED + style.BOLD + message + style.END)
    console.__writeToFile(message)

  @staticmethod
  def warn(msg: str):
    message = '( WARN )  [{}] --- {}'.format(datetime.datetime.now(), msg)
    print(color.YELLOW + style.BOLD + message + style.END)
    console.__writeToFile(message)

  @staticmethod
  def debug(msg: str):
    message = '( DEBUG ) [{}] --- {}'.format(datetime.datetime.now(), msg)
    print(color.BLUE + style.BOLD + message + style.END)
    
