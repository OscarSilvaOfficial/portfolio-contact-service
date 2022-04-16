from app.core.useCases import notify_new_contact_use_case, save_contact_use_case
from app.main.utils.exceptions import SaveContactException
from app.main.utils.exceptions import NotificationException
from app.ports import EmailSenderContract, ContactRepositoryContract
from app.core.models.contact import Contact
import logging


class ContactController:
  def __init__(self, contact_service: EmailSenderContract, contact_repository: ContactRepositoryContract):
    self.__email_sender_service = contact_service
    self.__contact_repository = contact_repository

  def index(self):
    return { "message": "Api UP" }

  def contact_service(self, contact: Contact):
    try:
      save_contact_use_case(self.__contact_repository, contact)
      logging.info(f'Contato salvo com sucesso!')
    except SaveContactException as e:
      logging.error(e.message)
    
    try:
      notify_new_contact_use_case(self.__email_sender_service, contact)
      logging.info(f'E-mail enviado')
    except NotificationException as e:
      logging.error(e.message)
      raise NotificationException()
    
    return { "message": "Email enviado com sucesso" }