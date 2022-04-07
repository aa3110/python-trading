def gap(a1='Close',a2='Open',df=None):
  ar,df[ar]=a1+a2+'_g',None
  df[ar]=(df[a1]-df[a2])/df[a1]*100
  return df[ar]