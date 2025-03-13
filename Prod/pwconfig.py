from configparser import ConfigParser, ExtendedInterpolation


def create_config():
    config = ConfigParser(interpolation=None)

    #Sections
    config.add_section('Password')

    #Password
    #config.set('Password','ODTS_password','rmAF-25$52{abcRT')
    config.set('Password','ODTS_password','vBrO-31$13{defRY') #3/13/25

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

