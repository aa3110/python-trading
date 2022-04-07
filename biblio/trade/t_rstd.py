def rstd(a1='Close',val1=None,df=None): 
  ar,df[ar]='std',None
  df[ar]=df[a1].rolling(val1).std()
  return df[ar]