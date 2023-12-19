import logging
from dirsync import sync

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('log.file.log', mode='w'))

source_path = 'C:/Projects/base'
target_path = 'C:/Projects/second'

sync(sourcedir=source_path, targetdir=target_path, action='sync', logger=logger) #for syncing one way
# sync(sourcedir=target_path, targetdir=source_path, action='sync', logger=logger) #for syncing the opposite way
