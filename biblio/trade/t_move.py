def move(a1='sma2',v1=2,df=None):
  ar2,df[ar2]='mv',None
  df[ar2]=df[a1].drop(index=0).reset_index(drop=True)  
  for i1 in range(df[ar2].shape[0]-v1,df[ar2].shape[0]):
    df[ar2][i1]=df[a1][i1]
  return df[ar2]