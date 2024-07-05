import I2C_LCD_driver
from time import *
from time import sleep
import class_rgb

    
mylcd = I2C_LCD_driver.lcd()
myled = class_rgb.LED()

while True:
    myled.turnOff(1)
    sleep(1) #1second
    mylcd.backlight(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("White!", 1,0)
    myled.white(1)
    sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Red!", 1,0)
    myled.red(1)
    sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Green!", 1,0)
    myled.green(1)
    sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Blue!", 1,0)
    myled.blue(1)
    sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Yellow!", 1,0)
    myled.yellow(1)
    sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Purple!", 1,0)
    myled.purple(1)
    sleep(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Light Blue!", 1,0)
    myled.lightBlue(1)
    sleep(1)
    mylcd.backlight(0)


