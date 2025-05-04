from fastapi import APIRouter

from lavacao_express.modules.user.models.user import User
from lavacao_express.modules.user.schemas.user import WriteUser
from lavacao_express.shared.deps import DbSession
from lavacao_express.modules.user.models.user import User, UserPermissions
from lavacao_express.modules.user.models.address import Address
from lavacao_express.modules.user.models.permissions import Permission
from lavacao_express.modules.user.models.profile import Profile


router = APIRouter(tags=["Account"])


@router.post("/client")
def create_client_user(_session: DbSession, user: WriteUser):
    profile_model = Profile(
        first_name=user.first_name,
        last_name=user.last_name,
        cpf=user.cpf,
        email=user.email,
        cell_phone=user.cell_phone,
        photo=user.photo,
    )
    user_model = User(
        login=user.email, password=user.password, is_client=True, profile=profile_model
    )
    with _session as session:
        session.add(user_model)
        session.add(profile_model)
        session.commit()
        session.refresh()
    user_model.addresses
    return user_model


@router.get("/{id_usuario}")
def detalhes_do_conta(id_usuario: int, filtro: str | None = None):
    pass
