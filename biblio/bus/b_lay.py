import numpy as np

def layout(df=[]):
  cash=10000
  broker=40 #USD
  tax=50 #%
  df['buy']=(df['qty']*df['value'])
  df['qty_sum']=df['qty'].cumsum()
  df['invest']=df['buy'].cumsum()
  df['market_value']=df['qty_sum']*df['value']
  df['rendite']=df['market_value']-df['invest']
  df['rendite%']=df['rendite']/df['invest']*100
  df['broker']=broker
  df['tax']=(df['rendite']-df['broker'])*tax/100
  df['tax']=np.where(df['tax']>0,df['tax'],0)
  df['profit']=df['rendite']-df['broker']-df['tax']
  df['cash']=cash-df['invest']
  df['depot']=df['market_value']+df['cash']
  df['broker_sum']=df['broker'].cumsum()
  df['tax_sum']=df['tax'].cumsum()
  df['cost_sum']=df['broker_sum']+df['tax_sum']
  return df