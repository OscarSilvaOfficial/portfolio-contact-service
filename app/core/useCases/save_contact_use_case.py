from app.core.models.contact import Contact
from app.ports.contact_repository_contract import ContactRepositoryContract
from app.main.utils.exceptions import SaveContactException


def save_contact_use_case(contact_repository: ContactRepositoryContract, contact: Contact):
  try:
    return contact_repository.save(contact)
  except Exception as e:
    raise SaveContactException()