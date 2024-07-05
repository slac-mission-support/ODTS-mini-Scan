#libraries
import RPi.GPIO as GPIO
from time import sleep

#disable warnings (optional)

GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 4
greenPin = 22
bluePin = 23
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

class LED:
    def red(self, state):
        if state == 1: #steady
            GPIO.output(redPin,GPIO.HIGH)
            GPIO.output(greenPin,GPIO.LOW)
            GPIO.output(bluePin,GPIO.LOW)
        if state == 2: #flashing
            for i in range(1,10):
                self.red(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)

    def green(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.LOW)
            GPIO.output(greenPin,GPIO.HIGH)
            GPIO.output(bluePin,GPIO.LOW)
        if state == 2:
            for i in range(1,10):
                self.green(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)
            
    def blue(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.LOW)
            GPIO.output(greenPin,GPIO.LOW)
            GPIO.output(bluePin,GPIO.HIGH)
        if state == 2:
            for i in range(1,10):
                self.blue(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)
            
    def white(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.HIGH)
            GPIO.output(greenPin,GPIO.HIGH)
            GPIO.output(bluePin,GPIO.HIGH)
        if state == 2:
            for i in range(1,10):
                self.white(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)

    def yellow(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.HIGH)
            GPIO.output(greenPin,GPIO.HIGH)
            GPIO.output(bluePin,GPIO.LOW)
        if state == 2:
            for i in range(1,10):
                self.yellow(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)
    
    def purple(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.HIGH)
            GPIO.output(greenPin,GPIO.LOW)
            GPIO.output(bluePin,GPIO.HIGH)
        if state == 2:
            for i in range(1,10):
                self.purple(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)
            
    def lightBlue(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.LOW)
            GPIO.output(greenPin,GPIO.HIGH)
            GPIO.output(bluePin,GPIO.HIGH)
        if state == 2:
            for i in range(1,10):
                self.lightBlue(1)
                sleep(0.05)
                self.turnOff(1)
                sleep(0.05)
        
    def turnOff(self, state):
        if state == 1:
            GPIO.output(redPin,GPIO.LOW)
            GPIO.output(greenPin,GPIO.LOW)
            GPIO.output(bluePin,GPIO.LOW)
    

    
