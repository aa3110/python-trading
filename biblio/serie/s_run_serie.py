from s_serie import serie
from f__init__ import file_read,file_save
from p__init__ import stock

def run_serie(stock='SIE',val1=7,df=None):
  stock2=stock+str(val1)
  df=file_read(stock)
  df=serie(val1,df)
  file=file_save(stock2,df)
  return