import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)
  df[a1][ws:we].plot(marker='o',figsize=(12,10),label=a1)
  plt.legend()
  return
# plot_pkt('Close2_rp',100,200,df)