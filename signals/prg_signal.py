from f__init__ import file_read,file_save
from m__init__ import msgbox, mail_sent
from playsound import playsound
import path_def.pat1

df=file_read('signal')

if df['Close_f'][0]==0:
  msgbox('test','title')
  mail_sent('subject','content as string')
  da=df['Close_f']
  file_save('message',da)
  playsound('x1.wma')