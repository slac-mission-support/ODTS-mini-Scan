import evdev
#from evdev import *
from evdev import categorize, InputDevice, ecodes
import signal, sys, time
import configparser
import os
from pathlib import Path
from time import sleep
scanning = True
keys = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

config = configparser.ConfigParser()
file_name = os.path.dirname(__file__) + '/config.ini'
config.read(file_name)
event_file = config.get('Scanner','event_file')
dev = evdev.InputDevice(event_file)

def scanBarcode():
  scanning = True
  while scanning is True:
    sleep(int(0.5))
    barcode = ''
    while True:
        event = dev.read_one()
        if event is None and barcode == '':
          #There are blank events in between characters, 
          #so we don't want to break if we've started
          #reading them
          break #nothing of importance, start a new read. 
        try:
          if event is not None:
            if event.type == ecodes.EV_KEY:
              data = categorize(event)
              if data.keystate == 0 and data.scancode != 42: # Catch only keyup, and not Enter
                if data.scancode == 28: #looking return key to be pressed
                  config = configparser.ConfigParser()
                  file_name = os.path.dirname(__file__) + '/config.ini'
                  config.read(file_name)
                  config.set('Scanner','barcode', str(barcode))
                  with open(file_name, 'w') as configfile:
                      config.write(configfile)
                      configfile.flush()
                      configfile.close()
                  scanning = False
                  return barcode
                else:
                  barcode += keys[data.scancode] # add the new char to the barcode
        except AttributeError:
          print("error parsing stream")
          return 'SOMETHING WENT WRONG'



