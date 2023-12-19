import logging
import argparse
from dirsync import sync
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("source_path")
parser.add_argument("target_path")
parser.add_argument("interval")
parser.add_argument("log_file_path")
args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file_path = args.log_file_path

logger.addHandler(logging.FileHandler(log_file_path, mode='a'))

source_path = args.source_path
target_path = args.target_path

interval = int(args.interval)

logger.info(f"Args received: {args}")

while True:
    sync(sourcedir=source_path, targetdir=target_path, action='sync')
    sleep(interval)

def my_sync(sourcedir: str, targetdir: str, logger: logger):
    pass
