import numpy as np

def fall(a1='bbh',df=None):
  ar,df[ar]=a1+'_f',None
  df[ar]=np.where(df[a1]<df[a1].shift(1),df[a1],0)
  return df[ar]