import oracledb
import pandas as pd
import LCD_messages
from time import sleep
# import class_rgb
# import I2C_LCD_driver
from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser()
#config = configparser.ConfigParser()
#config.read('config.ini')

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
		config.read('config.ini')
		odts_username = config.get('Database','ODTS_username')
		odts_password = config.get('Database','ODTS_password')
		odts_dsn = config.get('Database','ODTS_dsn')
		connection = oracledb.connect (
			user=odts_username,
			#password is hard coded but should move to a network location and called from here.
			password=odts_password,
			dsn=odts_dsn)

		if connection.is_healthy():
				from pandas import DataFrame
				print("Connection is Healthy on View 3 (issued with dosimeter #)")
				cursor = connection.cursor()
				query = cursor.execute("select * from DOSE_TEST.DOSIMETER_issued_VW where dosimeter = '" + dosimeter_id + "'")

				for row in query:
					# print("Dosimeter Number: ", row[0])
					# print("Wear Period: ", row[1])
					# print("SLAC ID: ", row[2])
					# print("Name: ", row[3])
					# print("email: ", row[4])
					# print("Supervisor SLAC ID: ", row[5])
					# print("Supervisor Name: ", row[6])
					# print("Supervisor email: ", row[7])
					# if row[8] is None:
						# print("Dosimeter is Unreturned")
					# else:
						# print("Return Date: ", str(row[8])[0:10])
					# print("oooooooooooooooooooooooo")
					numrows = str(query.rowcount)
					#print("View 3 row count: " + numrows)
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
			print("Unusable Connection.  Please check the database and network settings.")
			# mymessage.message8()
			# sleep(sleep_interval)
			# setup()
			
		cursor.close()
		connection.close()
