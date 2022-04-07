from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("serie")

  self.btn_runs = QPushButton(self)
  self.btn_runs.setText("run_serie_s")
  self.btn_runs.clicked.connect(self.run_serie_s)
  
  self.btn_runm = QPushButton(self)
  self.btn_runm.move(0,30)
  self.btn_runm.setText("run_serie_m")
  self.btn_runm.clicked.connect(self.run_serie_m)