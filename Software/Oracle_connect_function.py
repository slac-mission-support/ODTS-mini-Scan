import oracledb


connection = oracledb.connect (
	user="ODTSSCAN",
	#password is hard coded but should move to a network location and called from here.
	password="akUD,38%49]bnkDU",
	dsn="epndev.slac.stanford.edu/EPNQA")

dosi_number = '3851984I'
host_name = 'ODTSSCAN01'

if connection.is_healthy():
		print("Connection is Healthy")
		cursor = connection.cursor()
		result = cursor.callfunc('DOSE_TEST.UPDATE_RETURN_DT', str, [dosi_number, host_name])
		connection.commit()	
		print(result)
else:
	print("Unusable Connection.  Please check the database and network settings.")
			
cursor.close()
connection.close()
