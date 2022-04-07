from constant_plot import plr
import matplotlib.pyplot as plt
from p_pl_im import pl_im,sv_dp1

def plot_bb(a1='Close',a2='bbm',a3='bbh',a4='bbl',df=None):
  plt.figure(figsize=(12,10))
  # plt.plot(df[a1][100:300],color='green',linewidth=1.0)
  df[a1][plr[0]:plr[1]].plot(color='green',linewidth=1.0,linestyle='dashed')
  df[a2][plr[0]:plr[1]].plot(color='magenta',linewidth=1.0)
  df[a3][plr[0]:plr[1]].plot(color='blue',linewidth=1.0)
  df[a4][plr[0]:plr[1]].plot(color='blue',linewidth=1.0)
  plt.legend()
  return plt


def plot_bb5(df=None,da=None,*argv):
  n1=''.join(str(i1) for i1 in argv)
   
  plt.figure(figsize=(12,10),dpi=300)    
  for i2 in argv: df[i2].plot(linewidth=1.0); plt.legend()
  im=pl_im(plt) ; plt.close()
  
  da=save_pic(da,n1,im)
  
  # print(len(argv))
  return da


def save_pic(dp1=None,n1='',pic=''):
  dp1 = dp1.append({'nam': n1, 'pic': pic}, ignore_index=True)
  return dp1

def pl_im(plt=''):
  buf = io.BytesIO(); plt.savefig(buf, format='png')
  buf.seek(0); im = Image.open(buf)
  return im

def ini_dp1():
  dp1=pd.DataFrame(columns =['nam','pic'])
  return dp1
