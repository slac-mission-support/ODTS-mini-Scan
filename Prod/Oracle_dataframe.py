#used to find all dosimeters unreturned for a given person ID
#This is 4.2.3 in the specification
import oracledb
import pandas as pd

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


class return_dataframe_view1:
	
	def return_dataframe(self, person_id):
		
		connection = oracledb.connect (
			user="ODTSSCAN",
			#password is hard coded but should move to a network location and called from here.
			password="akUD,38%49]bnkDU",
			dsn="epndev.slac.stanford.edu/EPNQA")

		#person_id = '400777'

		if connection.is_healthy():
				from pandas import DataFrame
				print("Connection is Healthy on View 1 (Unreturned Person ID)")
				cursor = connection.cursor()
				query = cursor.execute("select * from DOSE_TEST.DOSIMETER_unreturned_VW where person_id =" + person_id)
				df = DataFrame(query)
				df.columns = ['Dosi#', 'Quarter', 'SLAC ID', 'Name', 'email', 'Sup SLAC ID', 'Sup Name', 'Sup email', 'return date']
				print(df)
				print()
				print()
				#return(df)
		else:
			print("Unusable Connection.  Please check the database and network settings.")
				
		cursor.close()
		connection.close()
