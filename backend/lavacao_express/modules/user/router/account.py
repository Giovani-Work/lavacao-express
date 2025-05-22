from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from backend.lavacao_express.modules.user.models import Address, Profile, User
from backend.lavacao_express.modules.user.schemas import (
    ReadAddress,
    ReadProfile,
    ReadUser,
    WriteUser,
)
from backend.lavacao_express.shared.deps import DbSession
from backend.lavacao_express.shared import utils


router = APIRouter(tags=["Account"])


@router.post("/client", response_model=ReadUser, status_code=status.HTTP_201_CREATED)
def create_client_user(session: DbSession, user_data: WriteUser) -> ReadUser:
    existing_user = session.exec(
        select(User).where(User.login == user_data.profile.cpf)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Login já está em uso"
        )

    # Verifica se o CPF já está cadastrado
    existing_profile = session.exec(
        select(Profile).where(Profile.cpf == user_data.profile.cpf)
    ).first()
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="CPF já cadastrado"
        )

    # Verifica se o email já está cadastrado
    existing_email = session.exec(
        select(Profile).where(Profile.email == user_data.profile.email)
    ).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado"
        )

    try:
        # Cria o perfil
        profile = Profile(
            first_name=user_data.profile.first_name,
            last_name=user_data.profile.last_name,
            cpf=user_data.profile.cpf,
            email=user_data.profile.email,
            cell_phone=user_data.profile.cell_phone,
            photo=user_data.profile.photo,
        )
        session.add(profile)
        session.commit()
        session.refresh(profile)

        # Cria o usuário com a senha criptografada
        user = User(
            login=profile.cpf,
            password=utils.get_password_hash(user_data.password),
            profile_id=profile.id,
            is_client=True,
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        # Cria o endereço
        address_list: list[Address] = []
        for address in user_data.address:
            _address = Address(
                street=address.street,
                number=address.number,
                district=address.district,
                city=address.city,
                state=address.state,
                postal_code=address.postal_code,
                user_id=user.id,
                is_principal=address.is_principal,
            )
            session.add(_address)
            session.commit()
            session.refresh(_address)
            address_list.append(_address)

        # Prepara a resposta
        response = ReadUser(
            id=user.id,
            profile=ReadProfile(
                id=profile.id,
                first_name=profile.first_name,
                last_name=profile.last_name,
                cpf=profile.cpf,
                email=profile.email,
                cell_phone=profile.cell_phone,
                photo=profile.photo,
            ),
            address=[
                ReadAddress(
                    id=addr.id,
                    street=addr.street,
                    number=addr.number,
                    district=addr.district,
                    city=addr.city,
                    state=addr.state,
                    postal_code=addr.postal_code,
                    is_principal=addr.is_principal,
                )
                for addr in address_list
            ],
        )
        return response

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar usuário: {str(e)}",
        )


@router.get("/{id_usuario}")
def detalhes_do_conta(id_usuario: int, session: DbSession):
    # Busca o usuário principal
    user = session.get(User, id_usuario)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Carrega o perfil relacionado
    profile = session.get(Profile, user.profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil do usuário não encontrado")

    # Carrega todos os endereços do usuário (considerando que pode ter múltiplos)
    addresses = session.exec(
        select(Address).join(User).where(User.id == id_usuario)
    ).all()

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

    # Converte os endereços para o modelo de leitura
    read_addresses = [
        ReadAddress(
            id=address.id,
            street=address.street,
            number=address.number,
            district=address.district,
            city=address.city,
            state=address.state,
            postal_code=address.postal_code,
            is_princiapl=address.is_principal,  # Note: corrigir typo no modelo se possível
        )
        for address in addresses
    ]

    # Retorna o usuário no formato do seu ReadUser
    return ReadUser(id=user.id, profile=read_profile, address=read_addresses)
