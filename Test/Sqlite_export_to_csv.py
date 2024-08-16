import pandas as pd
import sqlite3
import os
import datetime
from datetime import date
from datetime import timedelta
import configparser

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

class sqlite_export:

    def exported_data():
        config = configparser.ConfigParser()
        file_name = os.path.dirname(__file__) + '/config.ini'
        config.read(file_name)
        local_repo_path = config.get('Database','local_repo_path')        #raspberry pi path
        os.chdir(local_repo_path)
        #windows path
        #os.chdir("C:/Users/ryanford/OneDrive - SLAC National Accelerator Laboratory/Documents/GitHub/ODTS-mini-Scan/Test")
        local_db_name = config.get('Database', 'local_db_name')
        conn = sqlite3.connect(local_db_name, isolation_level=None,
                            detect_types=sqlite3.PARSE_COLNAMES)
        today = date.today() + timedelta(days = 1)
        #print(today)
        start = today - timedelta(days = 10)
        #print(start)
        query = ("SELECT HOST, TYPE, PERSON_ID, DOSI_ID, NAME, DATETIME FROM TRANSX WHERE DATETIME BETWEEN '" 
                + str(start) + "' AND '" + str(today) + "'")
        db_df = pd.read_sql_query(query, conn)

        from pandas import DataFrame

        df = DataFrame(db_df)
        sorted_df = df.sort_values(by=['DATETIME'], ascending = False)
        sorted_df['DATE'] = sorted_df['DATETIME'].str[:10]
        sorted_df['TIME'] = sorted_df['DATETIME'].str[11:19]

        sorted_df = sorted_df.drop(columns=['DATETIME'])
        return(sorted_df)

#p = sqlite_export.exported_data()
#print(p)
