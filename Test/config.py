from configparser import ConfigParser, ExtendedInterpolation


def create_config():
    config = ConfigParser(interpolation=None)

    config.add_section('General')
    config.add_section('Database')
    config.set('General','hostname', 'ODTSSCAN01')
    config.set('Database','local_repo_path', '/home/ryanford/Documents/ODTS-mini-Scan/Test')
    config.set('Database','local_db_name','test_records.db')
    config.set('Database','ODTS_server','epndev.slac.stanford.edu')
    config.set('Database','ODTS_username','ODTSSCAN')
    config.set('Database','ODTS_password',"akUD,38%49]bnkDU")
    config.set('Database','ODTS_db_name','epndev.slac.stanford.edu/EPNQA')
    config.set('General', 'foo', 'fighter')
    
    with open("config.ini", 'w') as configfile:
        config.write(configfile)
        configfile.flush()
        configfile.close()

    print("Config File Created")

if __name__== '__main__':
    create_config()


read_file = open("config.ini", "r")
content = read_file.read()
print("Contents:\n")
print(content)
read_file.flush()
read_file.close()

