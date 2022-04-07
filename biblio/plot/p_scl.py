from constant_plot import para,dir_p,plot_fig
import matplotlib.pyplot as plt
import numpy as np

def plot_scatter_line(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)
  df[a1][ws:we].dropna().plot(marker='o',figsize=(12,10),label=a1)
  plt.legend()
  if plot_fig==1: plt.savefig(dir_p+a1+str(para[0]), dpi=200)    
  return
#plot_line('Close2_rp',100,200,df)d