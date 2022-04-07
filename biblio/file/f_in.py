import pandas as pd
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")

from f_save import file_save
from f_new import new

def ini(a1='SIE_b'):
  df=new(a1)
  file_save(a1,df)
  return df