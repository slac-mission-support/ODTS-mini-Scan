import struct 
#import re
import pandas as pd
#from pandas import DataFrame
#import numpy as np


f = open( "/dev/input/event13", "rb" ); # Open the file in the read-binary mode'
while 1:

  data = f.read(24)
  df = pd.DataFrame(struct.unpack('4IHHI',data)).transpose()
  #print(df)
  dataframes = df
  df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  df.drop('a', axis = 1)
  filter_by = df['g'] == 1
  df_new = df[filter_by]
  if df_new.empty:
    continue

  print(df_new)


  #PRINT FORMAL = ( Time Stamp_INT , 0 , Time Stamp_DEC , 0 , type , code ( key pressed ) , value (press/release) )
