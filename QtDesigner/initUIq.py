from PyQt5.QtWidgets import QPushButton

def initUI(self):
  self.resize(900, 600)
  self.setGeometry(0, 0, 1500, 900)
  self.setWindowTitle("Qt")
  
  self.btn_backup = QPushButton(self)
  self.btn_backup.move(0,0)
  self.btn_backup.setObjectName("btn_backup")
  self.btn_backup.setText("backup (File)")
  self.btn_backup.clicked.connect(self.backup1)
    
  self.btn_restore = QPushButton(self)
  self.btn_restore.move(0,30)
  self.btn_restore.setObjectName("btn_restore")
  self.btn_restore.setText("restore (File)")
  self.btn_restore.clicked.connect(self.restore1)
    
  self.btn_daily = QPushButton(self)
  self.btn_daily.move(0,60)
  self.btn_daily.setObjectName("btn_daily")
  self.btn_daily.setText("daily (File)")
  self.btn_daily.clicked.connect(self.daily1)
  
  self.btn_bus = QPushButton(self)
  self.btn_bus.move(0,100)
  self.btn_bus.setObjectName("btn_bus")
  self.btn_bus.setText("bus (calc)")
  self.btn_bus.clicked.connect(self.bus1)
    
  self.btn_runs = QPushButton(self)
  self.btn_runs.move(0,130)
  self.btn_runs.setText("run_serie_s (calc)")
  self.btn_runs.clicked.connect(self.run_serie_s)
  
  self.btn_runs = QPushButton(self)
  self.btn_runs.move(0,160)
  self.btn_runs.setText("run_serie_m (calc)")
  self.btn_runs.clicked.connect(self.run_serie_m)
  
  self.btn_plot = QPushButton(self)
  self.btn_plot.move(0,200)
  self.btn_plot.setObjectName("btn_plot")
  self.btn_plot.setText("prg_plot (fig)")        
  self.btn_plot.clicked.connect(self.prg_plot)
  
      
  self.btn_plot_b = QPushButton(self)
  self.btn_plot_b.move(0,230)
  self.btn_plot_b.setObjectName("plot_bus (fig)")
  self.btn_plot_b.setText("plot_bus (fig)")        
  self.btn_plot_b.clicked.connect(self.plot_bus)
  
  # self.btn_filter1 = QPushButton(self)
  # self.btn_filter1.move(0,300)
  # self.btn_filter1.setObjectName("filter1")
  # self.btn_filter1.setText("filter1")        
  # self.btn_filter1.clicked.connect(self.filter1)
  
  self.btn_plot_table = QPushButton(self)
  self.btn_plot_table.move(0,260)
  self.btn_plot_table.setObjectName("plot_table (fig)")
  self.btn_plot_table.setText("plot_table (fig)")        
  self.btn_plot_table.clicked.connect(self.show_new_window)
  
  self.btn_sl_s = QPushButton(self)
  self.btn_sl_s.move(0,300)
  self.btn_sl_s.setText("slideshow_serie (sh)")
  self.btn_sl_s.clicked.connect(self.sl_serie)
  
  self.btn_sl_b = QPushButton(self)
  self.btn_sl_b.move(0,330)
  self.btn_sl_b.setText("slideshow_bus (sh)")
  self.btn_sl_b.clicked.connect(self.sl_bus)
  
  # self.btn_ex1 = QPushButton(self)
  # self.btn_ex1.move(0,330)
  # self.btn_ex1.setObjectName("extract")
  # self.btn_ex1.setText("extract")        
  # self.btn_ex1.clicked.connect(self.prg_ex)
  
  self.btn_shmb = QPushButton(self)
  self.btn_shmb.move(0,360)
  self.btn_shmb.setText("pic_bus_step (sh)")
  self.btn_shmb.clicked.connect(self.shmb)

  self.btn_shms = QPushButton(self)
  self.btn_shms.move(0,390)
  self.btn_shms.setText("pic_serie_step (sh)")
  self.btn_shms.clicked.connect(self.shms)