import numpy as np

def ins(a1=[],df=[]):
  df.loc[df.shape[0]] = np.array(a1)
  return df