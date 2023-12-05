import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('/home/ryanford/SQLite DB/ODTS_SYNC')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = '''SELECT * from ODTS_DATA'''
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("ID: ", row[0])
            print("system_id: ", row[1])
            print("name: ", row[2])
            print("email: ", row[3])
            print("return_date: ", row[4])
            print("dosimeter: ",row[5])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()