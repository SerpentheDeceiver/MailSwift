import os
from dotenv import load_dotenv #ENVIRONMENT VARIABLE
import smtplib #SMTPLIB SERVER
import email.mime.application #EMAIL
from email.mime.multipart import MIMEMultipart #MIMEMultipart
from email.mime.text import MIMEText #MIMEText

#CONSTANTS-->
SUBJECT = "Email Automation Testing"
ATT_FILE = ""


class EmailAutomation():

    def __init__(self):

        #LOADING
        load_dotenv('.env')

        #ENV VARIABLE'S
        self.EMAIL_ID = os.getenv('EMAIL_ID')
        self.PASSWORD = os.getenv('PASSWORD')
        self.SENDER_MAIL_ID = os.getenv('SENDER_MAIL_ID')

    def mailbody(self):
        #MSG
        MESSAGE = MIMEMultipart()
        MESSAGE['Subject'] = SUBJECT
        MESSAGE['From'] = self.EMAIL_ID
        MESSAGE['To'] = self.SENDER_MAIL_ID

        body = MIMEText("""
        <html>
          <body>
            <p>Hi Ganesh,</p>
            <p>I am fine! <b>How are you Nigga?</b>.</p>
            <p><i>This is an automated mail. No need to reply da punda.</i></p>
            <p>Thanks,<br>YOU!</p>
          </body>
        </html>
        """, "html")

        MESSAGE.attach(body)

        #ATTACHMENT FILE
        # filename = ATT_FILE
        # with open(filename, 'rb') as fp:
        #     att = email.mime.application.MIMEApplication(fp.read(), _subtype="txt")
        #     att.add_header('Content-Disposition', 'attachment', filename=filename)
        #     MESSAGE.attach(att)

        return MESSAGE

    def emailsender(self):

        #MESSAGE
        MESSAGE = self.mailbody()
        print(MESSAGE)

        #CONNECTION TO SMTPLIB SERVER
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(f"{self.EMAIL_ID}",f"{self.PASSWORD}")

            #SENDER
            connection.sendmail(from_addr=self.EMAIL_ID,
                                to_addrs=self.SENDER_MAIL_ID,
                                msg=MESSAGE.as_string())