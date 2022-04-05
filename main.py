from fastapi.middleware.cors import CORSMiddleware
from factories.email_sender import Factory
from models.forms import ContactPayload
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/contacts")
app = FastAPI(title="FastAPI Mangum Example", version='1.0.0')


@router.get("")
async def root():
  return {"message": "Api UP"}

@router.post("")
async def contact(payload: ContactPayload):
  sender = Factory.email_sender()
  sender.send(
    message=payload.message, 
    subject='Contato Portifólio | {} | {}'.format(payload.name, payload.email), 
  )
  return {"message": "Email enviado com sucesso"}

app.include_router(router)

app.add_middleware(
  CORSMiddleware,
  allow_origins="*",
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)
