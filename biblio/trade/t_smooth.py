def smooth(a1='Close',r1=7,loop=4,df=None):
  ar,df[ar]=a1+'_'+str(r1)+str(loop),None
  b1=df[a1] 
  for i in range(loop):
    b1=b1.rolling(r1).mean()
  df[ar]=b1
  return df[ar]