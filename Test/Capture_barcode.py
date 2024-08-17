program_status = True
barcode_input = str()
import I2C_LCD_driver
from time import sleep
from time import *
import class_rgb
import asyncio
import LCD_messages
import Oracle_connect_View3
import threading as th
import Oracle_connect_function as fn
import datetime
import Sqlite_insert_data
import ping
import configparser
import gmail_email as gmail


mygmail = gmail.send_email
mylcd = I2C_LCD_driver.lcd()
myled = class_rgb.LED()
mymessage = LCD_messages.messages()
mydata3 = Oracle_connect_View3.return_ODTS_view3()

myfunction = fn.Oracle_return_dosimeter
sqlite = Sqlite_insert_data.sqlite
myping = ping.network_ping
config = configparser.ConfigParser()
config.read('config.ini')
global new_return_date
new_return_date = datetime.datetime.now()
sleep_interval = float(config.get('General','sleep_time'))
reader_number = config.get('General','hostname')
slac_id = config.get('General','slac_ID')

def read_barcode_one_time():

	print("Awaiting input")
	barcode_input = input("Scan a barcode: ")
	print(f"Scanned barcode:  {barcode_input}")
	return barcode_input
	
def setup():
	myled.green(2)	
	mylcd.backlight(0)
	mylcd.lcd_clear()	
	mymessage.message1()
		
def shutdown():
	mylcd.lcd_clear()
	mylcd.backlight(0)
	
def read_barcode():
	barcode_input = read_barcode_one_time()
	mymessage.message2(barcode_input)
	global captured_barcode
	captured_barcode = barcode_input
	sleep(int(sleep_interval))	
	return(str(barcode_input))


def return_user():
	#[0] = full name
	#[1] = return date
	#[2] = slac ID
	#[3] = email
	#[4] = supervisor email
	#[5] = dosimeter number
	barcode = read_barcode()
	user = mydata3.return_info_view3(barcode)
	global return_date
	global slac_id
	global person_name
	global email_address	
	global sup_email
	global dosi_number	
	
	if not user:
		return_date = datetime.datetime.now()
		slac_id = 'N/A'
		person_name = 'N/A'
		email_address = 'N/A'
		sup_email = 'N/A'
		dosi_number = barcode
		mymessage.message10()
		sleep(int(sleep_interval))
		

	else:

		return_date = str(user[1])

		slac_id = user[2]

		person_name = user[0]
		if str(user) == 'None':
			mymessage.message7()
			sleep(int(sleep_interval))
		else:
			firstname = user[0].split(", ")[1]
			lastname = user[0].split(",")[0]
			mymessage.message6a(firstname, lastname)
		sleep(sleep_interval)

		email_address = user[3]

		sup_email = user[4]

		dosi_number = user[5]
	#populate the ini file so it's available for the email class
		config.set('General','slac_ID',str(slac_id))
		config.set('General','return_date', str(return_date))
		config.set('General','last_name',str(lastname))
		config.set('General','first_name',str(firstname))
		config.set('General','email', str(email_address))
		config.set('General','sup_email', str(sup_email))
		config.set('General','dosi_number', str(dosi_number))
		config.set('General','todays_date', str(new_return_date)[0:10])
		with open('config.ini', 'w') as f:
			config.write(f)

def return_dosimeter():
	function_result = myfunction.execute_return(str(captured_barcode), reader_number)
	if function_result == 'Already Returned':
		mymessage.message6b(return_date)
		sleep(int(sleep_interval))
	else:
		mymessage.message6b(str(datetime.datetime.now())[0:10])
		sleep(int(sleep_interval))
	
def write_to_sqlite():
	if str(return_date) == 'None':
		returndate = datetime.datetime.now() #new return date for today
		return_type = 'RETURN'
	elif slac_id == 'N/A':
		returndate =datetime.datetime.now()
		return_type = 'UNUSED'
		
	else:
		returndate = return_date  #what was queried from above, which does not store time component of the transaction
		print(return_date)
		return_type = 'REPEAT'
		
	sqlite.update_sqlite(reader_number, return_type, slac_id, captured_barcode, person_name, returndate)

while program_status:
	network = myping.check_ping()
	if network =='Network Active':
			setup()
			return_user()
			return_dosimeter()
			write_to_sqlite()
			if not return_date or return_date == 'None': 
				mygmail()
			else:  #don't send an email if this is a repeat scan.
				shutdown()
	else:
		myled.red(2)
		mymessage.message8()
		sleep(int(sleep_interval))
		
#def compose_email():
	
#def send_email():


