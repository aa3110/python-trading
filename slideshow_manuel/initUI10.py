from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("slideshow_manual")

  self.btn_sl_s = QPushButton(self)
  # self.btn_sl_s.setCheckable(True)
  self.btn_sl_s.move(0,0)
  self.btn_sl_s.setText("slideshow_serie_manual")
  self.btn_sl_s.clicked.connect(self.shms)
  
  self.btn_sl_b = QPushButton(self)
  # self.btn_sl_b.setCheckable(True)
  self.btn_sl_b.move(0,30)
  self.btn_sl_b.setText("slideshow_bus_manual")
  self.btn_sl_b.clicked.connect(self.shmb)