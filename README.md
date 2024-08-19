This script sends an email using Python's smtplib and email libraries. Here’s what the script does step by step:

1. Imports Required Libraries
EmailMessage: From the email.message module, it is used to create and structure the email.
ssl: Provides security by enabling SSL/TLS encryption.
smtplib: A library for sending emails using the Simple Mail Transfer Protocol (SMTP).
2. Set Up Email Details
Sender’s Email: email_sender is set to "sender@hotmail.com". This is the email address from which the message will be sent.
Sender’s Password: email_password is set to "not real password". This would be the password for the sender's email account. (In a real-world scenario, this password should be securely managed and not hard-coded.)
Receiver’s Email: email_reciver is set to "reciver@hotmail.com". This is the email address to which the email will be sent.
Subject: The email subject is "Dont forget to subscribe".
Body: The body of the email is a simple message.: Hola, this is a test. Bye.
3. Create the Email Message
Create EmailMessage Object: An EmailMessage object em is created.
Set Email Headers: The sender (From), recipient (To), and subject (Subject) fields of the email are set.
Set Content: The body of the email is set using em.set_content(body).
4. Create SSL Context
SSL Context: The script creates an SSL context using ssl.create_default_context(). This ensures that the connection to the email server is secure.
5. Send the Email
Connect to SMTP Server: The script connects to Gmail's SMTP server (smtp.gmail.com) on port 465 using smtplib.SMTP_SSL. This establishes a secure connection to send the email.
Login to SMTP Server: The script logs into the SMTP server using the sender's email credentials (email_sender and email_password).
Send the Email: The email is sent using smtp.sendmail, passing the sender's email, recipient's email, and the email message (em) converted to a string.
6. Close the Connection
Close SMTP Connection: The connection to the SMTP server is automatically closed when the with block is exited.
