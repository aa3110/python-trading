import matplotlib.pyplot as plt
import io
from PIL import Image
import pandas as pd


def pl_im(plt=''):
  buf = io.BytesIO(); plt.savefig(buf, format='png')
  buf.seek(0); im = Image.open(buf)
  return im

def sv_dp1(dp1=None,a1=[]):
  dp1 = dp1.append({'nam': a1[0], 'pic': a1[1]}, ignore_index=True)
  return dp1

def ini_dp1():
  dp1=pd.DataFrame(columns =['nam','pic'])
  return dp1
