from constant_plot import plr,para,nb,dir_p,plot_fig
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def plot_bb(a1='Close',a2='bbm',a3='bbh',a4='bbl',df=None):
  plt.figure(figsize=(12,10))
  # plt.plot(df[a1][100:300],color='green',linewidth=1.0)
  df[a1][plr[0]:plr[1]].plot(color='green',linewidth=1.0,linestyle='dashed')
  df[a2][plr[0]:plr[1]].plot(color='magenta',linewidth=1.0)
  df[a3][plr[0]:plr[1]].plot(color='blue',linewidth=1.0)
  df[a4][plr[0]:plr[1]].plot(color='blue',linewidth=1.0)
  plt.legend()
  return

def plot2(a1='Close',df=None):
  df[a1][plr[0]:plr[1]].plot(figsize=(12,10),label=a1)
  plt.legend()
  return

def plot_scatter(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)
  df[a1][ws:we].plot(marker='o',figsize=(12,10),label=a1)
  plt.legend()
  return
# plot_pkt('Close2_rp',100,200,df)

def plot_scatter_line(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)
  df[a1][ws:we].dropna().plot(marker='o',figsize=(12,10),label=a1)
  plt.legend()
  if plot_fig==1: plt.savefig(dir_p+a1+str(para[0]), dpi=200)    
  return
#plot_line('Close2_rp',100,200,df)d 

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

def ex_lin(w1=0,a=0,b=0):
  x = np.linspace(w1-10,w1+10,10)
  y=a*x+b
  plt.plot(x,y,color='magenta',linestyle=':')   
  return   

def plot_fit_line(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)#
  x=df[a1][ws:we].dropna().index.tolist()
  y=df[a1][ws:we].dropna().tolist()
  def fun(x, a, b): return a * x + b
  popt, _ = curve_fit(fun, x, y)
  a, b = popt
  yfit = [fun(xi,a,b) for xi in x]
  txt1='line'
  plt.plot(x, yfit,label=(a1,txt1))
  
  ex_lin(we,a,b)
  # plt.plot(x, y,marker='.')
  plt.legend()
  print('y = %.5f * x + %.5f' % (a, b))
  return a,b
#plot_fit_line('Close2_rp',100,200,df)

def plot_fit_lin_channel(a1='Close2_rp',ws=100,we=200,df=None):
  df[a1]=df[a1].replace(0,np.nan)#
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