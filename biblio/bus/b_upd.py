from f_read import file_read

def value_update(a1='SIE',df=[]):
  da=file_read(a1)
  for i in range(df.shape[0]):
    pos1=da[da['Date']==df['Date'][i]].index[0]
    df['value'][i]=da['Close'][pos1]
  return df