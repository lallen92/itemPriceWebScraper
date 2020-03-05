import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, content):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.sender_email = "maxPower@email.com"
        self.receiver_email = "example@email.com"
        self.password = "password123"
        self.content = content

    def sendEmail(self):
        '''
        	sendEmail:	Using SMTP protocol emails string containing the item details to user.


        '''
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email

        # Record the MIME types of both parts - text/plain and text/html.
        msgPart = MIMEText(self.content, 'plain')
        msg.attach(msgPart)

        try:
            # Create a secure SSL context
            context = ssl.create_default_context()

            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()
            server.starttls(context=context)
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, msg.as_string())
        except Exception as e:
            print(e)
        finally:
            server.quit()