import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

local_repo = config.get('Proxy','repo')
os.chdir(local_repo)
os.system("git pull --rebase")
