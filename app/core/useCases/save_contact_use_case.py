from app.core.models.contact import Contact
from app.ports.contact_repository_contract import ContactRepositoryContract


def save_contact_use_case(contact_repository: ContactRepositoryContract, contact: Contact):
  contact_repository.save(contact)
  return { "message": "Email enviado com sucesso" }