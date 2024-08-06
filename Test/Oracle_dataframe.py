#used to find all dosimeters unreturned for a given person ID
#This is 4.2.3 in the specification
import oracledb
import pandas as pd
from configparser import ConfigParser, ExtendedInterpolation

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

config = ConfigParser()
config = ConfigParser(interpolation=None)

class return_dataframe_view1:
	
	def return_dataframe(self, person_id):
		config.read('config.ini')
		odts_username = config.get('Database','ODTS_username')
		odts_password = config.get('Database','ODTS_password')
		odts_dsn = config.get('Database','ODTS_dsn')
		connection = oracledb.connect (
			user=odts_username,
			password=odts_password,
			dsn=odts_dsn)

		if connection.is_healthy():
				from pandas import DataFrame
				#print("Connection is Healthy on View 1 (Unreturned Person ID)")
				cursor = connection.cursor()
				query = cursor.execute("select * from DOSE_TEST.DOSIMETER_unreturned_VW where person_id =" + str(person_id))
				row = cursor.fetchone()
				if row is None:
					return(row)
				else:
					query = cursor.execute("select * from DOSE_TEST.DOSIMETER_unreturned_VW where person_id =" + str(person_id))
					df = DataFrame(query)
					df.columns = ['Dosi#', 'Quarter', 'SLAC ID', 'Name', 'Email', 'Sup SLAC ID', 'Sup Name', 'Sup Email', 'Return Date']
					df = df.drop(['Sup Name', 'Sup Email', 'Sup SLAC ID'], axis=1)
					df['Dosi#'] = df['Dosi#'].apply(lambda x: '***' + x[4:])		#obscure the first 4 characters of dosi# with asterix						
					return(df)

		else:
			print("Unusable Connection.  Please check the database and network settings.")
				
		cursor.close()
		connection.close()


