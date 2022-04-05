from PyQt5.QtWidgets import QFileDialog
from shutil import copy,unpack_archive,make_archive,rmtree
from os import makedirs,getcwd
from datetime import datetime
from pathlib import Path

def restore1(self):
    dir_path = r"d:\restore"
    rmtree(dir_path, ignore_errors=True)
    makedirs(dir_path)
    
    fileName1, filetype = QFileDialog.getOpenFileName (self, "select file", "D:\\backup\\", "All Files (*) ;; Excel Files (* .xls)")
    fileName1,fileName2=fileName1.replace("/", "\\"),fileName1.replace("backup", "restore")
    copy(src=fileName1,dst=fileName2)
    unpack_archive(fileName2,"D:/restore/")
    return self.statusBar().showMessage('done: restore')
          
def backup1(self):
    p1= getcwd()
    p2 = Path(p1)
    backup_dir=p2.parent.absolute()
    backup_file="D:\\backup\\"
    backup_file+='saved_{:%Y-%m-%d}'.format(datetime.now())
    make_archive(backup_file,"zip",backup_dir)
    return self.statusBar().showMessage('done: backup')