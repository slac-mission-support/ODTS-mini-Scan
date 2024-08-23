#RT870 python test demo
#ttl-232 readme
#by RTSCAN 20200901


import sys
import serial
import time

#default usb device /dev/ttyS0 115200 8n1
ser = serial.Serial("/dev/ttyACM0",115200,timeout=0.5)

print('serial test start ...')
if ser != None:
    print('serial ready...')
else:
    print('serial not ready')
    sys.exit()

ser.timerout=1 #read time out
ser.writeTimeout = 0.5 #write time out.

def printHex(str):
    for i in str:
        print('0x%02x'%ord(i)),
    print("")

def send_cmd(str):
    ser.write(str)
    time.sleep(0.2)
    t = ser.read(ser.in_waiting)
    print("reply")
    print(t)
    printHex(t)

def factory_defaults():
    print("factory_defaults")
    send_cmd("\x02\xf0\x03""0D0100"".")
    return

def set_baud_rate(baud):
    print("set_baud_rate")
    send_cmd("\x02\xf0\x03""060702"+baud+".")
    return

def get_baud_rate():
    print("get_baud_rate")
    send_cmd("\x02\xf0\x03""060702""?.")
    return
...
Please contact us to get full sample codes
