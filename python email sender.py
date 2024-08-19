from email.message import EmailMessage
import ssl
import smtplib
email_sender= "sender@hotmail.com"
email_password= "not real password"

email_reciver="reciver@hotmail.com"

subject="Dont forget to subscribe"
body="""Hola,
this is a test.
Bye"""

em=EmailMessage()
em['From']= email_sender
em["To"]=email_reciver
em["subject"]=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as smtp:
    
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
