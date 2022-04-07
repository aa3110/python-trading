from _another import AnotherWindow # MW2

def show_new_window(self, checked):
  self.w = AnotherWindow();self.w.show()
  return self.statusBar().showMessage('done: AnotherWindow')