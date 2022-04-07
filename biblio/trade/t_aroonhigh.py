def aroonhigh(a1='Close',val1=None,df=None):
  ar,df[ar]='Close_ah',None
  e1=val1+1
  for i in range(df[a1].shape[0]-1,e1,-1):
    lis=df[a1][i-val1:i+1]
    m1=max(lis)
    for counter, value in enumerate(lis):
      if (value==m1) :pos=counter
    df[ar][i]=100*pos/val1
  return df[ar]

def arh(a1='Close_ah',df=None):
  a2=a1+'_2'
  s1=df[a1].shape[0]-1
  
  ya=(df['Close'][200:s1]).max().round(0).astype(int);
  yi=(df['Close'][200:s1]).min().round(0).astype(int) 
  d1=(ya-yi)/100
  
  b1=df[a1]/100
  df[a2]=yi+(d1*b1)
  
  return df[a2]

def aroonhigh2(a1='Close',val1=None,df=None):
   aroonhigh(a1,val1,df)
   a2=a1+'_ah'
   arh(a2,df)
   return df
