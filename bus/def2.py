import path_def.pat1
from f__init__ import file_save,file_append
from b__init__ import bus_cr

def bus1(self): 
  df1,df2=bus_cr('SIE'),bus_cr('VOW')
  file_save('all',df1.iloc[-1:])
  file_append('all',df2.iloc[-1:])   
  return self.statusBar().showMessage('done: bus')