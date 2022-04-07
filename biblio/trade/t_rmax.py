def rmax(a1='Close',val1=None,df=None):
  ar,df[ar]='rmax',None
  df[ar]=df[a1].rolling(val1).max()
  return df[ar]