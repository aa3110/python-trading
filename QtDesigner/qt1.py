from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import path_def.pat1

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__() ; self.initUI()    
     
  from initUIq import initUI
    
  from def1 import backup1,restore1
   
  from def2 import bus1
  from def8 import run_serie_s,run_serie_m
   
  from def3 import daily1
  
  from def5 import  prg_plot
  from def6 import plot_bus
  from _def7 import show_new_window
    
  from def9 import sl_serie,sl_bus
  
  from def10 import shmb,shms
   
def window():
  app = QApplication(sys.argv)
  win = MyWindow(); win.show()
  sys.exit(app.exec_())
      
window()