import oracledb
import pandas as pd
import LCD_messages
from time import sleep
# import class_rgb
# import I2C_LCD_driver

#This is 4.2.1 in the specification
#Returns details for a dosimeter regardless of whether it was returned or not
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
# mymessage = LCD_messages.messages()
# sleep_interval = 2
# mylcd = I2C_LCD_driver.lcd()
# myled = class_rgb.LED()

class return_ODTS_view3:
	
	def setup():
		myled.green(2)	
		mylcd.backlight(0)
		mylcd.lcd_clear()	
		mymessage.message1()
		
	def return_info_view3(self, dosimeter_id):
		
		connection = oracledb.connect (
			user="ODTSSCAN",
			#password is hard coded but should move to a network location and called from here.
			password="akUD,38%49]bnkDU",
			dsn="epndev.slac.stanford.edu/EPNQA")

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
						return(row[3], str(row[8])[0:10], row[2])
		else:
			print("Unusable Connection.  Please check the database and network settings.")
			# mymessage.message8()
			# sleep(sleep_interval)
			# setup()
			
		cursor.close()
		connection.close()
