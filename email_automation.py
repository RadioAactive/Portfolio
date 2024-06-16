import smtplib , ssl

def email_auto(message):
    host = 'smtp.gmail.com'
    port = 465 

    reciever = ""
    password = ""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host , port ,context= context) as server:
        server.login(reciever , password)
        server.sendmail(reciever , reciever , message )
