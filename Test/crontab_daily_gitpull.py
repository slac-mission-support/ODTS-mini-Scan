import os
import configparser

config = configparser.ConfigParser()
file_name = os.path.dirname(__file__) + '/config.ini'
config.read(file_name)

local_repo = config.get('Proxy','repo')
os.chdir(local_repo)
os.system("git pull")
