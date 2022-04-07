import pandas as pd
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")

def file_read(a1='SIE_b'):
  file=path+a1+'.csv'
  df=pd.read_csv(file)
  print('-----READ---------------------:', file)
  return df