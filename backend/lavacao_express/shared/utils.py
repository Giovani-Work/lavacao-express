from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlmodel import select

from backend.lavacao_express.modules.user.models import User
from backend.lavacao_express.modules.user.schemas import TokenData
from backend.lavacao_express.shared.deps import DbSession
from backend.lavacao_express.shared import config


def verify_password(plain_password: str, hashed_password: str):
    return config.pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return config.pwd_context.hash(password)


# Funções auxiliares para JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire, "type": "refresh"})  # Mark as refresh token
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


async def get_current_user(
    session: DbSession, token: str = Depends(config.oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = session.exec(select(User).where(User.login == token_data.username)).first()
    if user is None:
        raise credentials_exception
    return user
