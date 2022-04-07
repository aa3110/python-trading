import pandas as pd
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")
from f_save import file_save

def new(a1='SIE_b'):
  h1=['Date','qty','value']
  df = pd.DataFrame(columns = h1)
  file_save(a1,df)
  return df