from constant_plot import para,nb,dir_p,plot_fig
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from p_ex import ex_lin

def plot_fit_lin_channel(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)
  x=df[a1][ws:we].dropna().index.tolist()
  y=df[a1][ws:we].dropna().tolist()
  def fun(x, a, b): return a * x + b
  popt, _ = curve_fit(fun, x, y)
  a, b = popt
  yfit = [fun(xi,a,b) for xi in x]
  txt1='line'
  plt.plot(x, yfit,label=(a1,txt1),color='magenta', linestyle='dashed')
  
  st1=(nb*df[a1][ws:we].dropna().rolling(para[0]).std().mean())
  plt.plot(x, yfit+st1,label=(a1,txt1,'+std'),color='magenta', linestyle='dashed')
  plt.plot(x, yfit-st1,label=(a1,txt1,'-std'),color='magenta', linestyle='dashed')
  ex_lin(we,a,b)
  ex_lin(we,a,b+st1)
  ex_lin(we,a,b-st1)
  # plt.plot(x, y,marker='.')
  plt.legend()
  if plot_fig==1: plt.savefig(dir_p+a1+str(para[0]), dpi=200)
  print('y = %.5f * x + %.5f' % (a, b))
  return a,b
#plot_fit_line('Close2_rp',100,200,df)