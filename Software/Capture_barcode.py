program_status = True
barcode_input = str()
import I2C_LCD_driver
from time import sleep
from time import *
import class_rgb
import asyncio
import LCD_messages

mylcd = I2C_LCD_driver.lcd()
myled = class_rgb.LED()
mymessage = LCD_messages.messages()

def read_barcode_one_time():
	print(f'\ncalled read_barcode_one_time()')
	print("awaiting input")
	barcode_input = input("Scan a barcode: ")
	print(f"Scanned barcode:  {barcode_input}")
	return barcode_input


	
while program_status:
		mylcd.backlight(0)
		myled.green(2)
		mylcd.lcd_clear()
		barcode_input = read_barcode_one_time()
		mymessage.message2(barcode_input)
		#mymessage.message6a("Ford", "Ryan")
		sleep(3)
		myled.turnOff(1)
		mylcd.lcd_clear()
		mylcd.backlight(0)
		program_status = False
	

