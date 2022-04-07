from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() ; self.initUI()

  from initUI10 import initUI
  from def10 import shms, shmb
            
def window():
    app = QApplication(sys.argv)
    win = MyWindow() ; win.show()
    sys.exit(app.exec_())

window()