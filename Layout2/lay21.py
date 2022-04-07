import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# import path_def.pat1

class MW(QMainWindow):
    def __init__(self):
      super().__init__() ; self.initUI()
      
    from initUI21 import initUI  
    from def21 import chkb_i,chkb_i2,chkb_s,ch_da,wi2,al1
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = MW() ; win.show()
  sys.exit(app.exec_())