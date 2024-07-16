import oracledb
import LCD_messages
from time import sleep
import class_rgb
import I2C_LCD_driver



mymessage = LCD_messages.messages()
sleep_interval = 2
mylcd = I2C_LCD_driver.lcd()
myled = class_rgb.LED()

class Oracle_return_dosimeter:
	
	def setup():
		myled.green(2)	
		mylcd.backlight(0)
		mylcd.lcd_clear()	
		mymessage.message1()
		
	def execute_return(dosi_number, host_name):

		connection = oracledb.connect (
			user="ODTSSCAN",
			#password is hard coded but should move to a network location and called from here.
			password="akUD,38%49]bnkDU",
			dsn="epndev.slac.stanford.edu/EPNQA")

#dosi_number = '6651225J'
#host_name = 'ODTSSCAN01'

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
			# mymessage.message8()
			# sleep(sleep_interval)
			# setup()
			
		cursor.close()
		connection.close()

#Error accoured: Dosimeter was already returned
#Success: Dosimeter return date updated
