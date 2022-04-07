import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
from pathlib import Path
import os
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, "inout\\")


def file_update(stock='SIE',start='2020-01-01'):
  file = path+stock+'.csv'
  print(file)
  
  def dl(stock=stock,start=start,end=str(date.today())):
    power=yf.Ticker(stock+'.DE')
    df=power.history(start=start, end=str(date.today()))
    df=df.drop('Dividends', axis=1)
    df=df.drop('Stock Splits', axis=1)
    return df

  def new(start=start):
    df=dl()
    df.to_csv(file, index=True, header=True, decimal='.', sep=',', float_format='%.6f')
    print('-----NEW--------------------:',file)
    return df
  
  def update():
    df=pd.read_csv(file)
    ds_1=df['Date'][(df.shape[0]-1)]
    da=dl(stock=stock,start=ds_1,end=str(date.today()))
   
    da=da.reset_index()
    da=da.drop(da.index[0])
    df=df.append(da)
    df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d')
    df=df.reset_index()
    df=df.drop('index', axis=1)
    df.to_csv(file, index=False, header=True, decimal='.', sep=',', float_format='%.6f')
    print('-----UPDATED--------------------:',file)
    return df

  if Path(file).is_file():
    df=update() 
  else:
    df=new()
  return df