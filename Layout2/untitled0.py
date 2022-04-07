import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

import pandas as pd
import os
from pathlib import Path
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent, "inout\\")

import io
from PIL import Image


import matplotlib.pyplot as plt
import io
from PIL import Image

a = [3, 5, 7, 5, 10]
b = [1, 2, 3, 4, 5]

plt.plot(a, b, 'g--')
# plt.grid()
# plt.xlabel('икс')
# plt.ylabel('игрек')
# plt.title('Название')

buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
im = Image.open(buf)
def get_plot():
    return im

get_plot()


import matplotlib.pyplot as plt
plr=(230,500)

# def file_read(a1='SIE_b'):
#   file=path+a1+'.csv'
#   df=pd.read_csv(file)
#   print('-----READ---------------------:', file)
#   return df

# def plot2(a1='Close',df=None):
#   b1=df[a1][plr[0]:plr[1]].plot(figsize=(12,10),label=a1)
#   # pic2=plt.legend()
  
#   buf = io.BytesIO()
#   b1.savefig(buf, format='png')
#   buf.seek(0)
#   im = Image.open(buf)
#   return #pic2


# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     # df=file_read('SIE7')
#     # pic1=plot2('Close',df)
    
    
#     widget = QLabel("Hello")
#     widget.Image.open(buf)
    
#     # widget.setPixmap(QPixmap('b1.png'))
    
#     widget.setScaledContents(True)
#     self.setCentralWidget(widget)
    
    
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec_()
