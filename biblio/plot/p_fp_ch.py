from constant_plot import para,nb,dir_p,plot_fig
import matplotlib.pyplot as plt
import numpy as np

def plot_fit_p_channel(a1='Close2_rp',ws=100,we=200,lev=2,df=None):
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
  plt.plot(x, yfit,label=(a1,txt1),color='magenta', linestyle='dashed')
  
  st1=(nb*df[a1][ws:we].dropna().rolling(para[0]).std().mean())
  plt.plot(x, yfit+st1,label=(a1,txt1,'+std'),color='magenta', linestyle='dashed')
  plt.plot(x, yfit-st1,label=(a1,txt1,'-std'),color='magenta', linestyle='dashed')
  if plot_fig==1: plt.savefig(dir_p+a1+str(para[0]), dpi=200)
  plt.legend()
  print("\ncoefficient value in case of linear polynomial:\n", z)
  return z
#plot_fit_p('Close2_rp',100,200,1,df)