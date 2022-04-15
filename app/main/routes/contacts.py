from fastapi import APIRouter
from app.adapters.controllers.contact_controller import ContactController
from app.main.factories.databases import mongodb_factory
from app.main.factories.email_sender import email_sender_factory
from app.adapters.repositories.contact_repository import ContactRepository
from app.models.contact import Contact

router = APIRouter(prefix="/contacts")

repository = ContactRepository(db=mongodb_factory())

controller = ContactController(
  contact_service=email_sender_factory(),
  contact_repository=repository
)

@router.get("")
async def root():
  return controller.index()

@router.post("")
async def notify_contact(contact: Contact):
  controller.save_contact(contact)
  return controller.notify_contact(contact)