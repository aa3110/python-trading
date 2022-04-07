def aroonlow2(a1='Close',val1=None,df=None):
  ar,df[ar]='Close_ah',None
  e1=val1+1; s1=df[a1].shape[0]-1
  for i in range(s1,e1,-1):
    lis=df[a1][i-val1:i+1]
    m1=max(lis)
    for counter, value in enumerate(lis):
      if (value==m1) :pos=counter
    df[ar][i]=100*pos/val1
  
    ya=(df[a1][200:s1]).max().round(0).astype(int)
    yi=(df[a1][200:s1]).min().round(0).astype(int) 
    d1=(ya-yi)/100
  
  df[ar+'_2']=yi+(d1*df[ar]/100)
  
  return df[ar+'_2']