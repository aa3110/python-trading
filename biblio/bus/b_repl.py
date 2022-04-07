
def repl(date1='2020-01-05', co1='value', val1=111.11,df=None):
  pos1=df[df['date']==date1].index[0]
  df[co1][pos1]=val1
  return df