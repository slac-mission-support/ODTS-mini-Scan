import sqlite3


def updateSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('ODTS_SYNC')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #sql_update_query = """Update SqliteDb_developers set salary = 10000 where id = 4"""
        sql_update_query = """UPDATE ODTS_DATA SET return_date = datetime('now','localtime') WHERE system_id = 789012"""


        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

updateSqliteTable()
