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


mylcd = I2C_LCD_driver.lcd()
myled = class_rgb.LED()
mymessage = LCD_messages.messages()
mydata3 = Oracle_connect_View3.return_ODTS_view3()

myfunction = fn.Oracle_return_dosimeter
reader_number = 'ODTSSCAN01'
sqlite = Sqlite_insert_data.sqlite
myping = ping.network_ping
config = configparser.ConfigParser()
config.read('config.ini')
global new_return_date
new_return_date = datetime.datetime.now()
sleep_interval = config.get('General','sleep_time')

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
	barcode = read_barcode()
	user = mydata3.return_info_view3(barcode)
	global return_date
	return_date = str(user[1])
	global slac_id
	slac_id = user[2]
	global person_name
	person_name = user[0]
	if str(user) == 'None':
		mymessage.message7()
		sleep(int(sleep_interval))
	else:
		firstname = user[0].split(", ")[1]
		lastname = user[0].split(",")[0]
		mymessage.message6a(firstname, lastname)
	sleep(sleep_interval)

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
		shutdown()
	else:
		myled.red(2)
		mymessage.message8()
		sleep(int(sleep_interval))
		
#def compose_email():
	
#def send_email():


