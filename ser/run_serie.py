from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() ; self.initUI()

  from initUI8 import initUI
  from def8 import run_serie_s,run_serie_m
               
def window():
    app = QApplication(sys.argv)
    win = MyWindow() ; win.show()
    sys.exit(app.exec_())
    
window()