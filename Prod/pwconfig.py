from configparser import ConfigParser, ExtendedInterpolation


def create_config():
    config = ConfigParser(interpolation=None)

    #Sections
    config.add_section('Password')

    #Password
    #config.set('Password','ODTS_password','rmAF-25$52{abcRT')
    #config.set('Password','ODTS_password','vBrO-31$13{defRY') #3/13/25
    #config.set('Password','ODTS_password','hQmy-51$15{defAN') #8/11/2025
    config.set('Password','ODTS_password','hQju-34$43{defZX') #1/9/2026
    
    with open("pwconfig.ini", 'w') as configfile:
        config.write(configfile)
        configfile.flush()
        configfile.close()

    print("Config File Created")

if __name__== '__main__':
    create_config()


read_file = open("pwconfig.ini", "r")
content = read_file.read()
print("Contents:\n")
print(content)
read_file.flush()
read_file.close()

