from app.adapters.controllers.contact_controller import ContactController
from app.main.factories.email_sender_factory import email_sender_factory
from app.main.factories import contact_repository_factory
from app.core.models.contact import Contact
from fastapi import APIRouter

router = APIRouter(prefix="/contacts")

controller = ContactController(
  email_sender_service=email_sender_factory(),
  contact_repository=contact_repository_factory()
)

@router.get("")
async def root():
  return controller.index()

@router.post("")
async def contact_service(contact: Contact):
  return controller.contact_service(contact)