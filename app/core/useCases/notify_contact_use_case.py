from app.core.models.contact import Contact
from app.main.utils.exceptions import NotificationException
from app.ports import EmailSenderContract


def notify_new_contact_use_case(email_sender_service: EmailSenderContract, contact: Contact):
  subject = 'Contato Portfólio'
  message = f'Nome: {contact.name}\nEmail: {contact.email}\nMensagem: {contact.message}'
  try:
    return email_sender_service.send(subject, message)
  except Exception:
    raise NotificationException()