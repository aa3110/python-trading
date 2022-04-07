import numpy as np
from t_sma import sma
from constant_serie import nb
from t_rstd import rstd

def bb(a1='Close',val1=None,df=None):
  df['bbm']=sma(a1,val1,df)
  df['bbh']=df['bbm']+(nb*rstd(a1,val1,df))
  df['bbl']=df['bbm']-(nb*rstd(a1,val1,df))
  df.drop(['std'], axis=1, inplace=True)
  return df['bbm'],df['bbh'],df['bbl']