import sys,os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,QPushButton
from glob import glob
from pathlib import Path
import path_def.pat1
from a_Cycle import Cycle

dir_p =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\picture\\bus")
imag1 = Cycle(glob(dir_p +"//"+"*.png"))

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("manuel Slideshow")
    self.setGeometry(0, 0, 0, 0)
    
    self.lab1 = QLabel("pic")
    self.lab1.setPixmap(QPixmap(next(imag1)))
    self.lab1.setFixedSize(800, 800)
    self.lab1.setScaledContents(True)
    self.setCentralWidget(self.lab1)
    
    self.btn1 = QPushButton(self)
    self.btn1.setText("next")
    self.btn1.clicked.connect(self.show_slides)
    
    self.btn2 = QPushButton(self)
    self.btn2.move(0,30)
    self.btn2.setText("back")
    self.btn2.clicked.connect(self.back_slides)
    
    
        
  def show_slides(self):
    self.lab1.setPixmap(QPixmap(next(imag1)))

  def back_slides(self):
    self.lab1.setPixmap(QPixmap(imag1.prev))

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = MainWindow() ; win.show()
  sys.exit(app.exec_())