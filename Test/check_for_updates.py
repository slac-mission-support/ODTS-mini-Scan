import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

local_repo = config.get('Database','git_pull_folder')
os.chdir(local_repo)
os.system("git pull")
