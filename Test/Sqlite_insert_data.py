import sqlite3
import os
import datetime
import configparser

class sqlite:
        
config = configparser.ConfigParser()
config.read('config.ini')
local_repo_path = config.get('Database','local_repo_path')
os.chdir(local_repo_path)
        
        def update_sqlite(host, type, person_ID, dosi_ID, name, datetime):
            try:
                config.read('config.ini')
                local_db_name = config.get('Database','local_db_name')
                sqliteConnection = sqlite3.connect(local_db_name)
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")

                sqlite_insert_with_param = """INSERT INTO TRANSX
                                  (host, type, person_ID, dosi_ID, name, datetime) 
                                  VALUES (?, ?, ?, ?, ?, ?);"""

                data_tuple = (host, type, person_ID, dosi_ID, name, datetime)
                cursor.execute(sqlite_insert_with_param, data_tuple)
                sqliteConnection.commit()
                print("Python Variables inserted successfully into SqliteDb_developers table")

                cursor.close()

            except sqlite3.Error as error:
                print("Failed to insert Python variable into sqlite table", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

#insertVaribleIntoTable('ODTSSCAN01', 'RETURN', 989898, '123456J', 'Frosio, Thomas', datetime.datetime.now() )
#insertVaribleIntoTable('ODTSSCAN01', 'RETURN', 878787, '123345J', 'Ding, Qi', datetime.datetime.now() )
