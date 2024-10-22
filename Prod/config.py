from configparser import ConfigParser, ExtendedInterpolation


def create_config():
    config = ConfigParser(interpolation=None)

    #Sections
    config.add_section('General')
    config.add_section('Database')
    config.add_section('Proxy')
    config.add_section('SMTP')
    config.add_section('Device_Info')
    config.add_section('Scanner')
    
    
    #General - Scanner Specific
    config.set('Device_Info','hostname', 'ODTSSCAN05')
    config.set('Device_Info','location', '028_105 Ryans Office')
    
    #General
    config.set('General','days_history', str(10)) #days history to email on crontab schedule
    config.set('General','slac_ID','')
    config.set('General','first_name','')
    config.set('General','last_name','')
    config.set('General','return_date','')
    config.set('General','email','')
    config.set('General','sup_email','')
    config.set('General','dosi_number','')
    config.set('General','todays_date','')       
    
    #General - Intervals
    config.set('General','sleep_time',str(1)) #speed up or slow down transaction at the reader
    config.set('General','led_flash_sleep_interval',str(0.05))    #speed of LED flashes for blink method
        
    #SMTPOUT
    config.set('SMTP','smtp_host','SMTPOUT.slac.stanford.edu')
    config.set('SMTP','smtp_port',str(25))
    config.set('SMTP','sender_email','esh-drep@slac.stanford.edu')
 
    
    # proxy info for git pull
    config.set('Proxy','proxy_hostname','mgmt-authproxy01')
    config.set('Proxy','proxy_port',str(3128))
    config.set('Proxy','repo','/home/ryanford/ODTS-mini-Scan')    

    #test database info
    # config.set('Database','local_repo_path', '/home/ryanford/ODTS-mini-Scan/Test')
    # config.set('Database','local_db_name','test_records.db')
    # config.set('Database','ODTS_server','epndev.slac.stanford.edu')
    # config.set('Database','ODTS_username','ODTSSCAN')
    # config.set('Database','ODTS_password',"akUD,38%49]bnkDU")
    # config.set('Database','ODTS_dsn','epndev.slac.stanford.edu/EPNQA')
    
    #PRODUCTION
    config.set('Database','local_repo_path', '/home/ryanford/ODTS-mini-Scan/Prod')
    config.set('Database','local_db_name','prod_records.db')
    config.set('Database','ODTS_server','epnprod.slac.stanford.edu')    
    config.set('Database','ODTS_username','ODTSSCAN')
    config.set('Database','ODTS_password',"akUD,38%49]bnkDU")
    config.set('Database','ODTS_dsn','epnprod.slac.stanford.edu/EPNPROD')   
    
    
    #scanner info
    config.set('Scanner','barcode','')
    config.set('Scanner','event_file','/dev/input/event0')
    
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

