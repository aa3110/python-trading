from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("daily")

  self.btn_daily = QPushButton(self)
  self.btn_daily.setObjectName("btn_daily")
  self.btn_daily.setText("daily")
  self.btn_daily.clicked.connect(self.daily1)