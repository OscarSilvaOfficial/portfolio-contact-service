from app.contracts.contact_repository_contract import ContactRepositoryContract
from app.contracts.db_contract import DBContract
from app.models.contact import Contact


class ContactRepository(ContactRepositoryContract):
  
  def __init__(self, db: DBContract):
    self.__db = db
  
  def save(self, contact: Contact):
    return contact