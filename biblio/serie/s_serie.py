from t__init__ import sma,bb,cci,gap,rmax,rmin,aroonhigh,aroonlow,aroonhigh2,aroonlow2,rise,fall,pkt_r,cross,cross_v,smooth,closen

def serie(val1,df='0'):
  closen('Close',df)  #'Closen
  sma('Close',val1,df)
  
  df['bbm'],df['bbh'],df['bbl']=bb('Close',val1,df)
  cci('Close',val1,df)
  gap('Close','Open',df)
  rmax('Close',val1,df)
  rmin('Close',val1,df)
  aroonhigh('Close',val1,df)
  aroonlow('Close',val1,df)
  aroonhigh2('Close',val1,df)
  aroonlow2('Close',val1,df)
  rise('Close',df)
  fall('Close',df)
  pkt_r('Close_r',df)
  cross('Close','bbh',df)
  cross_v('Close_ah',100,df)
  smooth('Close',7,4,df)
  df['vol']=(df['Volume']/df['Volume'].mean())
      
  print('-----SERIE created-------------------')
  
  return df