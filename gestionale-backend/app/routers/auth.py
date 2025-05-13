'''
Qui creiamo le rotte FastAPI per autenticazione (auth).

Usa SessionLocal() per accedere

Contiene la logica API REST

'''

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.database import get_db
from app import models, schemas

from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import LoginRequest

from app.utils.auth import get_current_user
from app.utils.jwt import create_access_token 



router = APIRouter()


@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Controlla se l'email è già registrata
    user_exist = db.query(models.user.User).filter(models.user.User.email == user.email).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="Email già registrata")

    # Hasha la password
    hashed_password = bcrypt.hash(user.password)

    # Crea nuovo utente
    new_user = models.user.User(
        nome=user.nome,
        cognome=user.cognome,
        email=user.email,
        hashed_password=hashed_password
    )

    # Salva nel DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
def login(data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.user.User).filter(models.user.User.email == data.email).first()

    if not user or not bcrypt.verify(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenziali non valide")

    access_token = create_access_token({"sub": str(user.id)}) #creazione token

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  #True in produzione con HTTPS
        samesite="lax"
    )

    return {
        "message": "Login effettuato con successo",
        "nome": user.nome,
        "cognome": user.cognome,
        "email": user.email
    }


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logout effettuato con successo"}


'''
get_current_user():

prende il token JWT dal cookie

lo decodifica

cerca l’utente nel database

se tutto va bene, lo restituisce
'''


@router.get("/me", response_model=schemas.UserResponse)
def read_me(current_user: models.user = Depends(get_current_user)):
    return current_user
