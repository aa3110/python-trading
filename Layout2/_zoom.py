from PyQt5.QtWidgets import QWidget,QToolButton,QLabel
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from pathlib import Path
import os,sys
import path_def.pat1
from a__init__ import PhotoViewer

dir_p =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent, "inout\\picture\\bus")
pic1=dir_p+"\\"+"buy.png"

class ZoomWindow(QWidget):
    def __init__(self):
        super(ZoomWindow, self).__init__()
        self.setGeometry(500, 300, 800, 600)
                   
        self.viewer=PhotoViewer(self)
       
        # 'Load image' button
        self.btnLoad = QToolButton(self)
        self.btnLoad.setText('Load image')        
        self.btnLoad.clicked.connect(self.loadImage)
                              
        # Arrange layout
        VBlay = QVBoxLayout(self)
        VBlay.addWidget(self.viewer)        
        VBlay.addWidget(self.btnLoad)

       

    def loadImage(self):
        self.viewer.setPhoto(QPixmap(pic1))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ZoomWindow();win.show()
    sys.exit(app.exec_())