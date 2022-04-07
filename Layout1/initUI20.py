from PyQt5.QtWidgets import QTabWidget,QLabel,QWidget,QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

# import path_def.pat1

def initUI_l1(self):  
  self.resize(1600, 800) # self.setGeometry(0, 0, 1600, 800) 
        
  self.tabs = QTabWidget()     
  self.tabs.setMovable(True)
              
  self.tab1,self.tab2,self.tab3,self.tab4 = QWidget(),QWidget(),QWidget(),QWidget()
  self.tabs.addTab(self.tab1,"Calc");self.tabs.addTab(self.tab2,"Chart");self.tabs.addTab(self.tab3,"depot");self.tabs.addTab(self.tab4,"signal")
              
  self.setCentralWidget(self.tabs)
               
  self.lab1 = QLabel(self.tab2)
  self.lab1.setGeometry(0, 50, 1200, 800) # self.lab1.setFixedSize(1200, 800)
  self.lab1.setPixmap(QPixmap("b1.png"))
  self.lab1.setScaledContents(True)
                     
  self.comboBox1 = QComboBox(self.tab2)
  self.comboBox1.setGeometry(QRect(0,20, 74, 22))
  self.comboBox1.setObjectName("comboBox1")
  self.comboBox1.addItem("VOW")
  self.comboBox1.addItem("BMW")
  self.comboBox1.addItem("SIE")
        
  self.comboBox2 = QComboBox(self.tab2)
  self.comboBox2.setGeometry(QRect(100, 20, 74, 22))
  self.comboBox2.setObjectName("comboBox2")
  self.comboBox2.addItem("sma")
  self.comboBox2.addItem("ema")
  self.comboBox2.addItem("bb")               