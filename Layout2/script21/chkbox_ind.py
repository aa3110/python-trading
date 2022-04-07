from tkinter import Tk, Checkbutton, IntVar
from functools import partial

def r2():
  def func(n):
      print(f'Selected {n + 1}') if var1[n].get() == 1 else print(f'Deselected {n + 1}')
      
  var1 = []
  app = Tk()
  
  lis1=['sma7',14,20]+['ema7',14,20]+['bb7',14,20]
  
  for i,fu in enumerate(lis1):
      var1.append(IntVar())
      Checkbutton(app, text=f'{fu} {i + 1}', variable=var1[i], command=partial(func, i)).grid(row=i%3, column=i//3)
        
  Checkbutton(app, text='exit', variable=None, command=app.destroy).grid(row=2, column=i+1)
  
  app.mainloop()
  
 