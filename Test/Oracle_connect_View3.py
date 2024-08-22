import oracledb
import pandas as pd
import LCD_messages
from time import sleep
from configparser import ConfigParser, ExtendedInterpolation
import os

config = ConfigParser()

#This is 4.2.1 in the specification
#Returns details for a dosimeter regardless of whether it was returned or not
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

config = ConfigParser(interpolation=None)

class return_ODTS_view3:
	
	def setup():
		myled.green(2)	
		mylcd.backlight(0)
		mylcd.lcd_clear()	
		mymessage.message1()
		
	def return_info_view3(self, dosimeter_id):
		file_name = os.path.dirname(__file__) + '/config.ini'
		config.read(file_name)
		odts_username = config.get('Database','ODTS_username')
		odts_password = config.get('Database','ODTS_password')
		odts_dsn = config.get('Database','ODTS_dsn')
		connection = oracledb.connect (
			user=odts_username,
			password=odts_password,
			dsn=odts_dsn)

		if connection.is_healthy():
				from pandas import DataFrame
				#print("Connection is Healthy on View 3 (issued with dosimeter #)")
				cursor = connection.cursor()
				query = cursor.execute("select * from DOSE_TEST.DOSIMETER_issued_VW where dosimeter = '" + dosimeter_id + "'")

				for row in query:
					numrows = str(query.rowcount)
					if numrows == '0':
						return("None")
					else: 
						return(row[3], str(row[8])[0:10], row[2], row[4], row[7], row[0])
						#[0] = full name
						#[1] = return date
						#[2] = slac ID
						#[3] = email
						#[4] = supervisor email
		else:
			#print("Unusable Connection.  Please check the database and network settings.")
			return
		cursor.close()
		connection.close()
