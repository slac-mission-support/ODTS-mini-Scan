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
        config.read('config.ini')
        local_repo_path = config.get('Database','local_repo_path')        #raspberry pi path
        os.chdir(local_repo_path)
        #windows path
        #os.chdir("C:/Users/ryanford/OneDrive - SLAC National Accelerator Laboratory/Documents/GitHub/ODTS-mini-Scan/Test")
        local_db_name = config.get('Database', 'local_db_name')
        conn = sqlite3.connect(local_db_name, isolation_level=None,
                            detect_types=sqlite3.PARSE_COLNAMES)
        today = date.today()
        yesterday = today - timedelta(days = 1)
        print(yesterday)
        db_df = pd.read_sql_query("SELECT HOST, TYPE, PERSON_ID, DOSI_ID, NAME, DATETIME FROM TRANSX", conn)
        #db_df.to_excel('database.xlsx', index=False)

        from pandas import DataFrame

        df = DataFrame(db_df)
        df['DATE'] = df['DATETIME'].str[:10]
        df['TIME'] = df['DATETIME'].str[11:19]
        #df.sort_values(['DATE', 'TIME'], ascending=[True, True], inplace=True)
        df = df.drop(columns=['DATETIME'])
        #df = df.sort_values('DATE')
        #df.style.set_table_styles()
        print(df)
        return(df)

