from app.contracts.contact_repository_contract import ContactRepositoryContract
from app.contracts.email_sender_contract import EmailSenderContract
from app.models.contact import Contact


class ContactController:
  def __init__(self, contact_service: EmailSenderContract, contact_repository: ContactRepositoryContract):
    self.__contact_service = contact_service
    self.__contact_repository = contact_repository

  def index(self):
    return { "message": "Api UP" }

  def notify_contact(self, contact: Contact):
    subject = 'Contato Portfólio'
    message = f'Nome: {contact.name}\nEmail: {contact.email}\nMensagem: {contact.message}'
    self.__contact_service.send(subject, message)
    return { "message": "Email enviado com sucesso" }
  
  def save_contact(self, contact: Contact):
    return self.__contact_repository.save(contact)
