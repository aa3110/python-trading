from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView

import path_def.pat1
from f__init__ import file_read

def initUI_p(self):            
      self.setGeometry(0, 20, 1000, 200)  # x, y, w, h
      self.setWindowTitle('Depot')
      
      self.tablewidget = QTableWidget(self)
      self.tablewidget.resize(1700, 700)           
      self.tablewidget.move(2, 2)
      df=file_read('all').round(decimals=1)
      r1,c1=df.shape[0],df.shape[1]
      self.tablewidget.setRowCount(r1+1)
      self.tablewidget.setColumnCount(c1) 
        
      self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                 
      for j in range(c1):self.tablewidget.setItem(0,j,QTableWidgetItem(str(df.columns[j])))
      for i in range(r1): 
        for j in range(c1):self.tablewidget.setItem(i+1,j,QTableWidgetItem(str(df.iloc[i, j])))  
     
def my_stylesheet():
    
    return """
    QLabel[color = "color_red"]
    { color : red;font-family: Trebuchet MS; font-style: normal; font-size:12pt; font-weight:700; }
    
    QLabel[color = "color_blue"]
    { color : blue;font-family: Trebuchet MS; font-style: normal; font-size:12pt; font-weight:700;}
    
    QLabel[backcolor = "bcolor_skyblue"]
    { background-color : skyblue}
    
    QLabel[backcolor = "bcolor_lightgreen"]
    { background-color : lightgreen}
    
    QLabel{ background-color: @mycolor;}
    
"""