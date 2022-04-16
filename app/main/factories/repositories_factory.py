from app.main.factories.databases_factory import mongodb_factory
from app.adapters.repositories import ContactRepository

def contact_repository_factory():
  return ContactRepository(db=mongodb_factory())