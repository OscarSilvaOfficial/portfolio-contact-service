from app.configs.enviroment import ROOT_EMAIL, ROOT_PASSWORD
from app.services.mail import EmailCredentials, EmailSender, SMTPServerInfo

class Factory:
  
  @staticmethod
  def email_sender():
    return EmailSender(
      credentials=EmailCredentials(ROOT_EMAIL, ROOT_PASSWORD), 
      smtp=SMTPServerInfo()
    )
