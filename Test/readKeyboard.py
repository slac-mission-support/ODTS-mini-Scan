import struct 
import re
import pandas as pd
from pandas import DataFrame
import numpy as np


f = open( "/dev/input/event13", "rb" ); # Open the file in the read-binary mode
while 1:
  data = f.read(24)
  data2 = struct.unpack('4IHHI',data)


  print(data2)

  #PRINT FORMAL = ( Time Stamp_INT , 0 , Time Stamp_DEC , 0 , type , code ( key pressed ) , value (press/release) )
