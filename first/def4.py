import path_def.pat1
from f__init__ import file_read,file_save
from p__init__ import stock2

def prg_ex(self):
  df=file_read(stock2)
  a1=df.shape[0]-1
  da=df[a1-2:a1+1]
  file_save('signal',da)
  return self.statusBar().showMessage('done: extract')