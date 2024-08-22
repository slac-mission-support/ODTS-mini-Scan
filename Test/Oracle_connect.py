#######used to find all dosimeters unreturned for a given person ID
#This is 4.2.3 in the specification
import oracledb
import pandas as pd
import LCD_messages
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

class return_ODTS_view1:

	def setup():
		myled.green(2)	
		mylcd.backlight(0)
		mylcd.lcd_clear()	
		mymessage.message1()
			
	def return_info(self, person_id):
		
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
				query = cursor.execute("select * from DOSE_TEST.DOSIMETER_unreturned_VW where person_id =" + person_id)
				for row in query:
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
						print("Return Date: ", str(row[8])[0:10])
					print("xxxxxxxxxxxxxxxxxxxxxxxx")
				
		else:
			print("Unusable Connection.  Please check the database and network settings.")
			
		cursor.close()
		connection.close()
