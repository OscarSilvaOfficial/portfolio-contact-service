from fastapi import APIRouter
from app.adapters.controllers.contact_controller import ContactController
from app.main.factories.email_sender import Factory
from app.models.contact import Contact

router = APIRouter(prefix="/contacts")
controller = ContactController(contact_service=Factory.email_sender())

@router.get("")
async def root():
  return controller.index()

@router.post("")
async def notify_contact(contact: Contact):
  return controller.notify_contact(contact)