def mail_sent(subject1='subject', content1='content as string'):
  import smtplib
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  # from constant import sender_address
  # from constant import sender_pass
  # from constant import receiver_address
  # from constant import server
  # from constant import port
   
  # mail send
  sender_address = 'm.cesena@web.de'
  sender_pass = 'vangoghring6'
  receiver_address = 'm.cesena@web.de'
  server='smtp.web.de'
  port=587
  #
    
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = subject1 
  mail_content = content1 
  message.attach(MIMEText(mail_content, 'plain'))
  
  #Create SMTP session for sending the mail
  session = smtplib.SMTP(server, port)
  session.starttls()
  session.login(sender_address, sender_pass)
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print('Mail Sent')
  return