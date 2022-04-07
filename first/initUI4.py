from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("extract")

  self.btn_extract = QPushButton(self)
  self.btn_extract.setObjectName("btn_extract")
  self.btn_extract.setText("prg_extract")        
  self.btn_extract.clicked.connect(self.prg_ex)