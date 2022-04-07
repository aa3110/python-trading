def arh(a1='Close',df=None):
  a2=a1+'_al'; a3=a2+'_2'
  s1=df[a1].shape[0]-1
  
  ya=(df[a1][200:s1]).max().round(0).astype(int);
  yi=(df[a1][200:s1]).min().round(0).astype(int) 
  d1=(ya-yi)/100
  
  df[a3]=yi+(d1*df[a2]/100)
  
  return df[a3]