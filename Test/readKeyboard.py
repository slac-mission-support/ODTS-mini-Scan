import struct 
#import re
import pandas as pd
#from pandas import DataFrame
#import numpy as np
global barcode

   
def data_function():
  f = open( "/dev/input/event13", "rb" ); # Open the file in the read-binary mode'
  while True:

    data = f.read(24)
    data2 = str(str(str(str(struct.unpack('4IHHI',data)).split(",")).replace("(","")).replace(")","")).replace(" ","")
    print(data2)


  #PRINT FORMAL = ( Time Stamp_INT , 0 , Time Stamp_DEC , 0 , type , code ( key pressed ) , value (press/release) )


def combine_data():
  mydata = [data_function()]
  for i in mydata:
      mydata2 = mydata.append(mydata)
  return(mydata2)
  


data_function()

