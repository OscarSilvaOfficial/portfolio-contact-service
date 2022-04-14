from app.infra.configs.enviroment import ROOT_EMAIL, ROOT_PASSWORD
from app.infra.services.mail import EmailCredentials, EmailSender, SMTPServerInfo

def email_sender_factory():
  return EmailSender(
    credentials=EmailCredentials(ROOT_EMAIL, ROOT_PASSWORD), 
    smtp=SMTPServerInfo()
  )
