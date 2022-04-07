import numpy as np
from t_move import move

def closen(a1='Close',df=None):
  ar,df[ar]=a1+'n',None
  ar2,df[ar2]=a1+str(2),None
  df[ar2]=df[a1].rolling(2).mean()
  df[ar]=move(ar2,2,df)
  df.drop(['Close2','mv'], axis=1, inplace=True)
  return df[ar]