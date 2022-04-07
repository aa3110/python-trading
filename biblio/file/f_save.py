import pandas as pd
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")

def file_save(a1='SIE_b',df=None):
  file=path+a1+'.csv'
  df.to_csv(file, index=False, header=True, decimal='.', sep=',', float_format='%.2f')
  print('-----SAVED--------------------:',file)
  return #file