from PyQt5.QtWidgets import QTabWidget,QLabel,QWidget,QToolButton
from PyQt5.QtGui import QPixmap


# import path_def.pat1

pic1="b1.png"
pic2="b1.png"

def initUI(self):
  self.resize(1600, 800) # self.setGeometry(0, 0, 1600, 800) 
    
  self.tabs = QTabWidget()     
  self.tabs.setMovable(True)
              
  self.tab1,self.tab2,self.tab3,self.tab4 = QWidget(),QWidget(),QWidget(),QWidget()
  self.tabs.addTab(self.tab1,"Calc");self.tabs.addTab(self.tab2,"Chart");self.tabs.addTab(self.tab3,"depot");self.tabs.addTab(self.tab4,"signal")
              
  self.setCentralWidget(self.tabs)
  
  self.lab1 = QLabel(self.tab2)
  
  self.lab1.setGeometry(0, 50, 1200, 600) # self.lab1.setFixedSize(1200, 800)
  self.lab1.setPixmap(QPixmap(pic1))
  self.lab1.setScaledContents(True)
      
  self.lab2 = QLabel(self.tab2)
  self.lab2.setGeometry(0, 650, 1200, 100) # self.lab1.setFixedSize(1200, 800)
  self.lab2.setPixmap(QPixmap(pic2))
  self.lab2.setScaledContents(True)
  
  
  self.btn_chkb_s = QToolButton(self.tab2)
  self.btn_chkb_s.move(0,20)
  self.btn_chkb_s.setText("chkbox_st")
  self.btn_chkb_s.clicked.connect(self.chkb_s)          
               
  self.btn_chkb_i = QToolButton(self.tab2)
  self.btn_chkb_i.move(100, 20)
  self.btn_chkb_i.setText("chkbox_ind")
  self.btn_chkb_i.clicked.connect(self.chkb_i)
  
  self.btn_chkb_i2 = QToolButton(self.tab2)
  self.btn_chkb_i2.move(200, 20)
  self.btn_chkb_i2.setText("chkbox_ind2")
  self.btn_chkb_i2.clicked.connect(self.chkb_i2)
            
  self.btn_da = QToolButton(self.tab2)
  self.btn_da.move(300, 20)
  self.btn_da.setText("chkbox_date_range")
  self.btn_da.clicked.connect(self.ch_da) 
    
  self.btn_w2 = QToolButton(self.tab2)
  self.btn_w2.move(900, 20)
  self.btn_w2.setText("w2")
  self.btn_w2.clicked.connect(self.wi2)
  
  self.btn_w2 = QToolButton(self.tab2)
  self.btn_w2.move(1300, 20)
  self.btn_w2.setText("alert")
  self.btn_w2.clicked.connect(self.al1)