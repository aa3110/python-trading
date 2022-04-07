import numpy as np

def cross(a1='Close',a2='bbh',df=None):
  ar,df[ar]=a1+a2+'_c',None
  df[ar]=np.where((df[a1]>=df[a2])&(df[a1].shift(1)<=df[a2].shift(1)),df[a2],0)
  df[ar]=np.where((df[a1]<=df[a2])&(df[a1].shift(1)>=df[a2].shift(1)),-df[a2],df[ar])
  return df[ar]