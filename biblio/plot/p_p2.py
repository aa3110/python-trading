from constant_plot import plr
import matplotlib.pyplot as plt

def plot2(a1='Close',df=None):
  df[a1][plr[0]:plr[1]].plot(figsize=(12,10),label=a1)
  plt.legend()
  return