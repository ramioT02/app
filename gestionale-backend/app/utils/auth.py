from jose import JWTError, jwt
from fastapi import Request, HTTPException, status, Depends
from app.core.config import settings
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User

def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token mancante")

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token invalido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token non valido")

    user = db.query(User).filter(User.id == int(user_id)).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="Utente non trovato")

    return user


