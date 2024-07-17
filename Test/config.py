import configparser

def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'hostname': 'ODTSSCAN01', 'local_repo_path': '/home/ryanford/Documents/ODTS-mini-Scan/Test'}
    config['Database'] = {'local_db_name':'test_records.db', 'ODTS_server': 'epndev.slac.stanford.edu', 
                          'ODTS_username':'ODTSSCAN', 'ODTS_password':'akUD,38%49]bnkDU', 
                          'ODTS_db_name':'epndev.slac.stanford.edu/EPNQA'}
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    create_config