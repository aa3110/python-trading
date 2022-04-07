from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class MyWindow(QMainWindow):
    def __init__(self):
      super().__init__() ; self.initUI_p()
    
    from initUI7 import initUI_p
          
 
app = QApplication(sys.argv)
win = MyWindow() ; win.show()
sys.exit(app.exec_())
 
if __name__ == '__main__':   
  MyWindow()