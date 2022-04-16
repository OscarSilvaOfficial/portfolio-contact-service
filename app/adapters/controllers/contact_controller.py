from app.core.useCases import notify_new_contact_use_case, save_contact_use_case
from app.main.utils.exceptions import SaveContactException
from app.main.utils.exceptions import NotificationException
from app.ports import EmailSenderContract, ContactRepositoryContract
from app.core.models.contact import Contact
import logging

logger = logging.getLogger(__name__)

class ContactController:
  def __init__(self, email_sender_service: EmailSenderContract, contact_repository: ContactRepositoryContract):
    self.__email_sender_service = email_sender_service
    self.__contact_repository = contact_repository

  def index(self):
    return { "message": "Api UP" }

  def contact_service(self, contact: Contact):
    try:
      save_contact_use_case(self.__contact_repository, contact)
      logger.info(f'Contato salvo com sucesso!')
    except SaveContactException as e:
      logger.error(str(e))
    
    try:
      notify_new_contact_use_case(self.__email_sender_service, contact)
      logger.info(f'E-mail enviado')
    except NotificationException as e:
      logger.error(str(e))
      raise NotificationException()
    
    return { "message": "Email enviado com sucesso" }