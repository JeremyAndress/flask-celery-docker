import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LoggingConf:
    LOG_FILENAME_INFO = BASE_DIR+'/logs/info.log'
    LOG_FILENAME_ERROR = BASE_DIR+'/logs/error.log'
    LOG_FILENAME_CRITICAL = BASE_DIR+'/logs/critical.log'
    FORMAT = '%(asctime)s,%(msecs)05.1f %(message)s'
    DATEFMT = '%m/%d/%Y %H:%M:%S'

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = logging.FileHandler(LoggingConf.LOG_FILENAME_INFO)
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(LoggingConf.FORMAT)
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

