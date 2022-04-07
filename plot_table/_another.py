from PyQt5.QtWidgets import QTableWidget

import path_def.pat1
from f__init__ import file_read

class AnotherWindow(QTableWidget):
   
    def __init__(self):
        super().__init__() ; self.initUI_p()  
        
    from initUI7 import initUI_p              