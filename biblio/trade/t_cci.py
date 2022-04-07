import numpy as np
from t_sma import sma
from t_rstd import rstd

def cci(a1='Close',val1=None,df=None):
  ar,df[ar]='CCI',None
  df[ar]=(df[a1]-sma(a1,val1,df))/(0.01*rstd(a1,val1,df))
  df.drop(['std'], axis=1, inplace=True)
  return df[ar]

def c1(a1='CCI',df=None):
  a2=a1+'_2'
  s1=df[a1].shape[0]-1
  
  ya=(df['Close'][200:s1]).max().round(0).astype(int)
  yi=(df['Close'][200:s1]).min().round(0).astype(int) 
  d1=(ya-yi)/200
  
  b1=(df[a1]+100)/200
  df[a2]=yi+(d1*b1)
  
  return df[a2]

def cci2(a1='Close',val1=None,df=None):
   a2=cci(a1,val1,df)
   c1(a2,df)
   return df
