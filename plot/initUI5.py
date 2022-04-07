from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("plot")

  self.btn_plot = QPushButton(self)
  self.btn_plot.setObjectName("btn_plot")
  self.btn_plot.setText("prg_plot")        
  self.btn_plot.clicked.connect(self.prg_plot)