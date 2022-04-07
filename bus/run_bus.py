from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() ; self.initUI()

  from initUI2 import initUI
  from def2 import bus1
            
def window():
    app = QApplication(sys.argv)
    win = MyWindow() ; win.show()
    sys.exit(app.exec_())

window()