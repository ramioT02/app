'''
app/database.py

Questo file si occupa della connessione a PostgreSQL e della gestione delle sessioni DB in SQLAlchemy.

permetti di creare/modificare/queryare le tabelle nel DB.

Fa da ponte tra FastAPI e PostgreSQL.

'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Creazione dell'engine
engine = create_engine(settings.DATABASE_URL)

# Sessione del DB (usata per comunicare col DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base da cui ereditano tutti i modelli
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()