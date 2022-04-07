import numpy as np

def cross_v(a1='aroonlow',val11=100,df=None):
  ar=a1+str(val11)+'_v'
  df[ar]=None
  if val11>0 :
    df[ar]=np.where(df[a1]>=val11,df[a1],0)
  else :
    df[ar]=np.where(df[a1]<=val11,df[a1],0)
  return df[ar]