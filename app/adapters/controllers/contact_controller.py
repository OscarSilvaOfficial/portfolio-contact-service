from app.core.useCases import notify_new_contact_use_case, save_contact_use_case
from app.ports.contact_repository_contract import ContactRepositoryContract
from app.ports.email_sender_contract import EmailSenderContract
from app.core.models.contact import Contact


class ContactController:
  def __init__(self, contact_service: EmailSenderContract, contact_repository: ContactRepositoryContract):
    self.__email_sender_service = contact_service
    self.__contact_repository = contact_repository

  def index(self):
    return { "message": "Api UP" }

  def contact_service(self, contact: Contact):
    notify_new_contact_use_case(self.__email_sender_service, contact)
    return save_contact_use_case(self.__contact_repository, contact)
