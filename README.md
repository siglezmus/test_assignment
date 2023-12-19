# test_assignment
Script that syncronizes two given folders with set interval

Script should be run from venv containing requirements from requirements.txt file

Example of command to execute the script for windows:
python main.py C:/Projects/base C:/Projects/second 5 log_file.log

Arguments after 'python main.py' must be in following order source_path, target_path, interval, log_file_path
Path arguments can be absolute or relative in string format
Interval must be an integer and interval is provided in seconds