from fastapi import FastAPI
from app.database import Base, engine
from app.models import user  
from app.routers import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crea le tabelle nel DB al primo avvio
Base.metadata.create_all(bind=engine)

# Importa tutte le rotte da auth.py
app.include_router(auth.router, prefix="/api")
