import logging
import argparse
import os
from dirsync import sync
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("source_path")
parser.add_argument("target_path")
parser.add_argument("interval")
parser.add_argument("log_file_path")
args = parser.parse_args()


if not os.path.isdir(args.source_path):
    raise ValueError("Error: Source directory does not exist.")
source_path = args.source_path

if not os.path.isdir(args.target_path):
    raise ValueError("Error: Target directory %s does not exist.")
target_path = args.target_path

if not args.interval.isnumeric():
    raise ValueError("Error: interval must be integer.")
interval = int(args.interval)

if not args.log_file_path[-4:] == ".log" and os.path.isdir(args.log_file_path[:args.log_file_path.rfind("/")]):
    raise ValueError("Error: Log file path does not exist.")
log_file_path = args.log_file_path
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler(log_file_path, mode='a'))

while True:
    sync(sourcedir=source_path, targetdir=target_path, action='sync')
    sleep(interval)

def my_sync(sourcedir: str, targetdir: str):
    pass
