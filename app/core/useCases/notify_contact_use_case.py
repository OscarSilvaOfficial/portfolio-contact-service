from app.core.models.contact import Contact
from app.ports.email_sender_contract import EmailSenderContract


def notify_contact_use_case(email_sender_service: EmailSenderContract, contact: Contact):
  subject = 'Contato Portfólio'
  message = f'Nome: {contact.name}\nEmail: {contact.email}\nMensagem: {contact.message}'
  return email_sender_service.send(subject, message)