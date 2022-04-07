def rmin(a1='Close',val1=None,df=None):
  ar,df[ar]='rmin',None
  df[ar]=df[a1].rolling(val1).min()
  return df[ar]