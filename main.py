import logging
import argparse
import os
from time import sleep
import shutil

def copy(sourcedir: str, targetdir: str):
    try:
        logger.info(f"From source: {sourcedir} copying to target: {targetdir}")
        print(f"From source: {sourcedir} copying to target: {targetdir}")
        shutil.copy(sourcedir, targetdir)
    except:
        logger.info("File already exists")
        print("File already exists")

def my_sync(sourcedir: str, targetdir: str):

    for folder_name, subfolders, filenames in os.walk(sourcedir):
        logger.info(f"Current folder is {folder_name}")
        print(f"Current folder is {folder_name}")
        for subfolder in subfolders:
            logger.info(f"Subfolder of {folder_name}:{subfolder}")
            print(f"Subfolder of {folder_name}:{subfolder}")
            try:
                new_path = folder_name.replace(sourcedir, targetdir)
                os.mkdir(new_path+"\\"+subfolder)
            except:
                logger.info("Folder already exists")
                print("Folder already exists")
        for filename in filenames:
            new_path = folder_name.replace(sourcedir, targetdir)
            file = folder_name+"\\"+filename
            copy(file, new_path)


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

if not (args.log_file_path[-4:] == ".log" and (os.path.isdir(args.log_file_path[:args.log_file_path.rfind("/")]) or args.log_file_path.rfind("/") == -1)):
    raise ValueError("Error: Log file path does not exist.")
log_file_path = args.log_file_path
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler(log_file_path, mode='a'))

while True:
    my_sync(sourcedir=source_path, targetdir=target_path)
    sleep(interval)
