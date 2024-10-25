import oracledb
import LCD_messages
import class_rgb
import I2C_LCD_driver
from configparser import ConfigParser, ExtendedInterpolation
import os

config = ConfigParser()
config2 = ConfigParser()

mymessage = LCD_messages.messages()
sleep_interval = 2
mylcd = I2C_LCD_driver.lcd()
myled = class_rgb.LED()
config = ConfigParser(interpolation=None)

class Oracle_return_dosimeter:
	
	def setup():
		myled.green(2)	
		mylcd.backlight(0)
		mylcd.lcd_clear()	
		mymessage.message1()
		
	def execute_return(dosi_number, host_name):
		file_name = os.path.dirname(__file__) + '/config.ini'
		file_name_pw = os.path.dirname(__file__) + '/pwconfig.ini'
		config.read(file_name)
		odts_username = config.get('Database','ODTS_username')
		odts_dsn = config.get('Database','ODTS_dsn')

		config2.read(file_name_pw)
		odts_password = config2.get('Password','ODTS_password')

		connection = oracledb.connect (
			user=odts_username,
			#password is hard coded but should move to a network location and called from here.
			password=odts_password,
			dsn=odts_dsn)

		if connection.is_healthy():
				print("Connection on View 1 Function is Healthy")
				cursor = connection.cursor()
				result = cursor.callfunc('DOSE_TEST.UPDATE_RETURN_DT', str, [dosi_number, host_name])
				connection.commit()	
				if result == 'Error accoured: Dosimeter was already returned':
					return('Already Returned')
				elif result == 'Success: Dosimeter return date updated':
					return('Successfully Returned')
				else:
					return('Invalid')
					
		else:
			print("Unusable Connection.  Please check the database and network settings.")
			mymessage.message8()
			sleep(sleep_interval)
			setup()
			
		cursor.close()
		connection.close()

#Error accoured: Dosimeter was already returned
#Success: Dosimeter return date updated
