import numpy as np
from t_move import move

def pkt_r(a1='bbh_r',df=None):
  ar,df[ar]=a1+'p',None
  df[ar]=np.where((df[a1]==0) & (df[a1].shift(1)!=0),df[a1].shift(1),0)
  df[ar]=move(ar,2,df)
  df[ar]=df[ar].replace(0,np.nan)
  df.drop(['mv'], axis=1, inplace=True)
  return df[ar]