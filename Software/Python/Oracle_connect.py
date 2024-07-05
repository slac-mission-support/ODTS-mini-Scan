import oracledb

connection = oracledb.connect (
	user="ODTSSCAN",
	#password is hard coded but should move to a network location and called from here.
	password="akUD,38%49]bnkDU",
	dsn="epndev.slac.stanford.edu/EPNQA")

person_id = '484229'

if connection.is_healthy():
		print("Connection is Healthy")
		cursor = connection.cursor()
		for row in cursor.execute("select * from DOSE_TEST.DOSIMETER_unreturned_VW where person_id =" + person_id):
			print("Dosimeter Number: ", row[0])
			print("Wear Period: ", row[1])
			print("SLAC ID: ", row[2])
			print("Name: ", row[3])
			print("email: ", row[4])
			print("Supervisor SLAC ID: ", row[5])
			print("Supervisor Name: ", row[6])
			print("Supervisor email: ", row[7])
			if row[8] is None:
				print("Dosimeter is Unreturned")
			else:
				print("Return Date: ", row[8])
			print("------------------")
else:
	print("Unusable Connection.  Please check the database and network settings.")
		
cursor.close()
connection.close()
