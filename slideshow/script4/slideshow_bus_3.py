import tkinter as tk
from tkinter import Tk, Label ,Checkbutton
from PIL import Image, ImageTk
from pathlib import Path 
from itertools import cycle  
import os 

dir_p =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\picture\\bus")
w,h,delay=800,800,2000

app=tk.Tk() ; app.geometry(str(w)+"x"+str(h))
lab=Label() ; lab.pack()

def Phot(p1="a1.png"):
  i1=Image.open(p1) ; i1 = i1.resize((w,h), Image.ANTIALIAS)
  pic=ImageTk.PhotoImage(i1)
  lab.config(image=pic)  
  return pic

def show_slides():
    lab.config(image=next(pic))
    app.after(delay, show_slides)

pic=cycle(map(lambda x :Phot(x) ,list(Path(dir_p).glob("*.png"))))
show_slides()

app.mainloop()