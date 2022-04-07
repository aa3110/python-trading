from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("bus")

  self.btn_bus = QPushButton(self)
  self.btn_bus.setObjectName("btn_bus")
  self.btn_bus.setText("bus")
  self.btn_bus.clicked.connect(self.bus1)