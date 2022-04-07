# https://www.geeksforgeeks.org/create-a-sideshow-application-in-python/
# https://stackoverflow.com/questions/6582387/image-resize-under-photoimage

# import required modules
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from pathlib import Path    

# dir_p="D:\\prg\\script\\qt_designer\\slideshow\\a"
dir_p="D:\\prg\\script\\python\\TA-Lib\\220102\\inout\\picture\\serie"

# adjust window
root=tk.Tk() ;root.geometry("600x600")
l=Label() ; l.pack()


w,h=600,600
x = 0

def f1(p1="a1.png"):
  i1=Image.open(p1)
  i1 = i1.resize((w,h), Image.ANTIALIAS)
  im=ImageTk.PhotoImage(i1)
  l.config(image=im)  
  return im

im=list(map(lambda j :f1(j) ,list(Path(dir_p).glob("*.png"))))
  
def move():
    global x
    l.config(image=im[x])
    x +=1
    if x!=len(im) : root.after(2000, move)

move()
  
root.mainloop()