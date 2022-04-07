def cleaner(a1='Close',val1=None,df=None):
  a1=a1+str(val1)+'_r'
  ar=a1+'p'
  df.drop([ar+'2_mv'], axis=1, inplace=True)
  df.drop(['Close2','Close22_mv'], axis=1, inplace=True)
  return df