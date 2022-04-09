from fastapi import APIRouter
from app.factories.email_sender import Factory
from app.models.forms import ContactPayload

router = APIRouter(prefix="/contacts")

@router.get("")
async def root():
  return { "message": "Api UP" }

@router.post("")
async def contact(payload: ContactPayload):
  sender = Factory.email_sender()
  subject = 'Contato Portfólio'
  message = f'Nome: {payload.name}\nEmail: {payload.email}\nMensagem: {payload.message}'
  sender.send(subject, message)
  return { "message": "Email enviado com sucesso" }