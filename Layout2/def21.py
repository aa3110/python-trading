from PyQt5.QtGui import QPixmap
from script21.chkbox_st import r1
from script21.chkbox_ind import r2
from script21.chkbox_ind2 import r2b
from script21.chkbox_date_range import r4


def chkb_s(self):
  r1()
  return self.statusBar().showMessage('done: chkbox_st')

def chkb_i(self):
  r2()
  return self.statusBar().showMessage('done: chkbox_ind')

def chkb_i2(self):
  r2b()
  return self.statusBar().showMessage('done: chkbox_ind2')
  
def ch_da(self):
  r4() 
  return self.statusBar().showMessage('done: chkbox_date_range')

def wi2(self):
  from _another import AnotherWindow
  self.xa = AnotherWindow();self.xa.show()  
  return self.statusBar().showMessage('done: AnotherWindow')

def al1(self):
  print('alert') 
  return self.statusBar().showMessage('done: alert')