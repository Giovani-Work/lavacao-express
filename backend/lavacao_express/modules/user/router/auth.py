from datetime import timedelta
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from backend.lavacao_express.modules.user.models import Profile, User
from backend.lavacao_express.modules.user.schemas import (
    ReadProfile,
    Token,
    UserLogged,
    UserLogin,
)
from backend.lavacao_express.shared import config, utils
from backend.lavacao_express.shared.deps import DbSession

router = APIRouter(tags=["Auth"])


@router.post("/login")
def login_usuario(login_data: UserLogin, session: DbSession):
    # Busca o usuário no banco de dados
    user = session.exec(select(User).where(User.login == login_data.login)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verifica a senha
    if not utils.verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = utils.create_access_token(data={"sub": user.login})
    refresh_token = utils.create_refresh_token(data={"sub": user.login})

    # Busca o perfil do usuário
    profile = session.get(Profile, user.profile_id)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perfil do usuário não encontrado",
        )

    # Converte o perfil para o modelo de leitura
    read_profile = ReadProfile(
        id=profile.id,
        first_name=profile.first_name,
        last_name=profile.last_name,
        cpf=profile.cpf,
        email=profile.email,
        cell_phone=profile.cell_phone,
        photo=profile.photo,
    )

    return UserLogged(
        id=user.id,
        login=user.login,
        profile=read_profile,
        access_token=Token(token=access_token, token_type="bearer"),
        refresh_token=Token(token=refresh_token, token_type="bearer"),
    )


@router.post("/change-password")
def alterar_senha(id_usuario: int):
    pass
