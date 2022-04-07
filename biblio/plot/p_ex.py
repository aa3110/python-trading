import matplotlib.pyplot as plt
import numpy as np

def ex_lin(w1=0,a=0,b=0):
  x = np.linspace(w1-10,w1+10,10)
  y=a*x+b
  plt.plot(x,y,color='magenta',linestyle=':')   
  return   