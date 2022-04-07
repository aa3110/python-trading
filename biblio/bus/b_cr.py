from f_read import file_read
from f_save import file_save
from f_append import file_append
from b_upd import value_update
from b_lay import layout

def bus_cr(stock='SIE'):
  stock1=stock+'_inp'
  df,da=file_read(stock1),file_read(stock)
    
  dic = {'Date': da['Date'][da.shape[0]-1],'qty': 0}
 
  df = df.append(dic, ignore_index = True)
  df['value'],df['stock']=0.01,stock
   
  df=value_update(stock,df)
  
  file_save(stock+'_inp2',layout(df))
  return df