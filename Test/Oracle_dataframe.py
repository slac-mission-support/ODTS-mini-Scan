#used to find all dosimeters unreturned for a given person ID
#This is 4.2.3 in the specification
import oracledb
import pandas as pd
import configparser

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

config = configparser.ConfigParser()
config.read('config.ini')

class return_dataframe_view1:
	
	def return_dataframe(self, person_id):
		
		odts_username = config.get('Database','odts_username')
		odts_password = config.get('Database','odts_password')
		odts_dsn = config.get('Database','odts_dsn')
		connection = oracledb.connect (
			user=odts_username,
			#password is hard coded but should move to a network location and called from here.
			password=odts_password,
			dsn=odts_dsn)

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
				return(df)
		else:
			print("Unusable Connection.  Please check the database and network settings.")
				
		cursor.close()
		connection.close()

return_dataframe_view1.return_dataframe(400777)