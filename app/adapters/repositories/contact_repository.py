from app.ports.contact_repository_contract import ContactRepositoryContract
from app.ports.db_contract import DBContract
from app.models.contact import Contact


class ContactRepository(ContactRepositoryContract):
  
  def __init__(self, db: DBContract):
    self.__db = db
  
  def save(self, contact: Contact):
    self.__db.create(contact.dict())
    return contact