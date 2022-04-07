def aroonlow(a1='Close',val1=None,df=None):
  ar,df[ar]='Close_al',None
  e1=val1+1
  for i in range(df[a1].shape[0]-1,e1,-1):
    lis=df[a1][i-val1:i+1]
    m1=min(lis)
    for counter, value in enumerate(lis):
      if (value==m1) :pos=counter
    df[ar][i]=100*pos/val1
  return df[ar]