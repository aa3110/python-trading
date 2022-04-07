from constant_plot import plr,para,dir_p,plot_fig
import matplotlib.pyplot as plt

def plot_aroon1(st1='CCI',st2='Closehigh',st3='Close',df=None):
  fig, ax = plt.subplots()
 
  t=df['Date'].index.values.astype(int)
  
  ax.set_xlabel('Date')
    
  color1 = 'tab:blue'
  ax.set_ylabel(st1, color=color1)
  ax.plot(t[plr[0]:plr[1]], df[st1][plr[0]:plr[1]], color=color1,linewidth=1.0)
  ax.tick_params(axis='y', labelcolor=color1)
  
  color2 = 'tab:orange'
  ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis
  ax2.set_ylabel(st2, color=color2)  # we already handled the x-label with ax
  ax2.plot(t[plr[0]:plr[1]], df[st2][plr[0]:plr[1]], color=color2,linewidth=0.5)
  ax2.tick_params(axis='y', labelcolor=color2)
  
  fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
  color3 = 'tab:green'
  ax3 = ax.twinx()
  ax3.set_ylabel(st3, color=color3)
  ax3.spines['right'].set_position(('outward', 40))
  ax3.plot(t[plr[0]:plr[1]], df[st3][plr[0]:plr[1]], color=color3,linewidth=1.0,linestyle='dashed')
  ax3.tick_params(axis='y', labelcolor=color3)
  if plot_fig==1: plt.savefig(dir_p+st1+st2+st3+str(para[0]), dpi=200)    
  return