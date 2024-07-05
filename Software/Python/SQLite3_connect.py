import sqlite3

con=sqlite3.connect("ODTSSCAN01.db")

cur=con.cursor()

#SETUP MAIN TABLE
#cur.execute("CREATE TABLE return_history(host, transx_type, transx_date, dosinumber, slacid)")

#SAMPLE INSERT INTO QUERY
cur.execute("""
	INSERT INTO return_history VALUES
		('ODTSSCAN01', 'RETURN', DATETIME('now'),'00123458J', 400777),
		('ODTSSCAN01', 'RETURN', DATETIME('now'),'00123459J', 123456)
""")
con.commit()

for row in cur.execute("SELECT * FROM return_history"):

	print(row)
	
# CLEAR THE TABLE:
# cur.execute("DELETE from return_history;")
# con.commit()
# for row in cur.execute("SELECT * FROM return_history"):
	# print(row)
	
cur.close()
con.close()

