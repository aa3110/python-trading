from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("plot_bus")

  self.plot_b = QPushButton(self)
  self.plot_b.setObjectName("bus_plot")
  self.plot_b.setText("bus_plot")
  self.plot_b.clicked.connect(self.plot_bus)