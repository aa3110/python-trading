import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MW(QMainWindow):
    def __init__(self):
      super().__init__(); self.initUI_l1()
    from initUI20 import initUI_l1
           
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    win = MW() ; win.show()
    sys.exit(app.exec_())