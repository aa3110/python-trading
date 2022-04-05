from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(200, 200, 300, 300)
  self.setWindowTitle("backup_restore")
 
  self.btn_backup = QPushButton(self)
  self.btn_backup.setObjectName("btn_restore")
  self.btn_backup.setText("backup")
  self.btn_backup.clicked.connect(self.backup1)
    
  self.btn_restore = QPushButton(self)
  self.btn_restore.move(0,30)
  self.btn_restore.setObjectName("btn_restore")
  self.btn_restore.setText("restore")
  self.btn_restore.clicked.connect(self.restore1)