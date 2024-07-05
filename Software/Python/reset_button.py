#RESET BUTTON
#pin 18 (IO18) and ground

# from gpiozero import Button
# button = Button(18)

# button.wait_for_press()
# print('You pushed me')


import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def Restart(channel):
	os.system("sudo shutdown -r now")
	
GPIO.add_event_detect(18, GPIO.FALLING, callback = Restart, bouncetime = 2000)

while 1:
		time.sleep(1)
