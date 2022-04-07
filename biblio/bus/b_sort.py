
def sort(a1='date',df=[]):
  df=df.sort_values(by=[a1])
  return df