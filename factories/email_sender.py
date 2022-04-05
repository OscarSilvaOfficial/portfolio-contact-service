from services.mail import EmailCredentials, EmailSender, SMTPServerInfo
import os

class Factory:
  
  @staticmethod
  def email_sender():
    email=os.environ.get('EMAIL')
    password=os.environ.get('PASSWORD')
    smtp_server_info = SMTPServerInfo()
    email_credentials = EmailCredentials(email, password)
    return EmailSender(credentials=email_credentials, smtp=smtp_server_info)
