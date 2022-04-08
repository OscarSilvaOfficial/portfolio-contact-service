from configs.cors import CORS
from fastapi import FastAPI
from routes.controllers import router as contacts_router

app = FastAPI(title="FastAPI Contact", version='1.0.0')

app.include_router(contacts_router)
app.add_middleware(**CORS)
