import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
sections = config.sections()
print(sections)
output = config.get('General','hostname')
print(output)

