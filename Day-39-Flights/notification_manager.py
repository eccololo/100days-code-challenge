from email.message import EmailMessage
from decouple import config
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.


    def __init__(self):

        self.recipient = "<recipient-email>"
        self.sender = "<sender-email>"
        self.subject = "Flight Notification"
        self.EMAIL_KEY = config("EMAIL_KEY")


    def send_notification_email(self, notification_text):

        try:
            msg = EmailMessage()
            msg["Subject"] = self.subject
            msg["From"] = self.sender
            msg["To"] = self.recipient

            msg.set_content(notification_text)

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()

                connection.login(
                    user=self.sender,
                    password=self.EMAIL_KEY
                )

                connection.send_message(msg)

            print("✅ Email sent successfully!")

            return True

        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed - check EMAIL_KEY or login.")
            return False

        except smtplib.SMTPRecipientsRefused:
            print("❌ Recipient email rejected.")
            return False

        except smtplib.SMTPException as e:
            print(f"❌ SMTP error occurred: {e}")
            return False

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False