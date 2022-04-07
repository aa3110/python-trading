from script5.sh_man_bus1 import MW
from script5.sh_man_serie1 import MainWindow

def shmb(self, checked):
  self.tx = MW() ; self.tx.show()
  return self.statusBar().showMessage('done: shmb')  

def shms(self, checked):
  self.tw = MainWindow() ; self.tw.show()
  return self.statusBar().showMessage('done: shms')