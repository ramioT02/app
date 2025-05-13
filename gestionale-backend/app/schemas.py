'''

in questo modulo ci occupiamo della comunicazione tra front react e fastApi nel back per la validazione dei dati
'''

from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    #riceve i dati dal front in json al back pre registrazione
    nome: str
    cognome : str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    #invia i dati dal back al front post registrazione
    id: int
    nome: str
    cognome: str
    email: EmailStr
    ruolo: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str