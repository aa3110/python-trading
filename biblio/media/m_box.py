def msgbox(msg='test', title='title'):
  import pymsgbox
  global response
  pymsgbox.alert(msg, title)
  response = pymsgbox.prompt('sell / buy?')
  print(response)
  return response