import smtplib , ssl
import os

def email_auto(message):
    host = 'smtp.gmail.com'
    port = 465 

    reciever = ""
    password =  os.getenv("")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host , port ,context= context) as server:
        server.login(reciever , password) # type: ignore
        server.sendmail(reciever , reciever , message )
