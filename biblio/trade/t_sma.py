def sma(a1='Close',val1=None,df=None):
  ar,df[ar]='sma',None
  df[ar]=df[a1].rolling(val1).mean()
  return df[ar]