import path_def.pat1
from f__init__ import file_update

def daily1(self):
  file_update('SIE','2020-01-02')
  file_update('VOW','2020-01-02')  
  return self.statusBar().showMessage('done: daily')