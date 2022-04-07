from constant_plot import plr,para,dir_p,plot_fig
import matplotlib.pyplot as plt

def col_plot(st='bbm',ind1='bbm_r',df=None):
  plt.figure(figsize=(12,10))
  p2=plr[1]
  if plr[1]>df.shape[0]-1: p2=df.shape[0]-1 
  df[['Closen',st]][plr[0]:p2].plot(figsize=(12,10))
  for i in range(plr[0],p2):
    if df[ind1][i]==0:
      plt.plot(df[st][i-1:i+1],marker='',color='red',linewidth=1.0)
    else :
      plt.plot(df[st][i-1:i+1],marker='',color='green',linewidth=1.0)
  if plot_fig==1: plt.savefig(dir_p+st+ind1+str(para[0]), dpi=200)    
  #plt.show() 
  return