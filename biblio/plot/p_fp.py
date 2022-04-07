from constant_plot import para,dir_p,plot_fig
import matplotlib.pyplot as plt
import numpy as np

def plot_fit_p(a1='Close2_rp',ws=100,we=200,lev=2,df=None):
  x=df[a1][ws:we].dropna().index
  y=df[a1][ws:we].dropna()
  z = np.polyfit(x, y, lev)
  z = z[::-1]
  w1,yfit=0,[]
  for xi in x:
    for j in range(0,lev+1):
      w1+= z[j]*xi**j
    yfit.append(w1)
    w1=0
  txt1=('level=',lev) 
  plt.plot(x, yfit,label=(a1,txt1))
  plt.legend()
  if plot_fig==1: plt.savefig(dir_p+a1+str(para[0]), dpi=200)
  print("\ncoefficient value in case of linear polynomial:\n", z)
  return z
#plot_fit_p('Close2_rp',100,200,1,df)