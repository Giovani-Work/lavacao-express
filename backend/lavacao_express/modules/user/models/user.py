from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

from lavacao_express.modules.user.models.permissions import Permission
from lavacao_express.modules.user.models.profile import Profile


class UserPermissions(SQLModel, table=True):
    __tablename__: str = "user_permissions"

    id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    users: list["User"] = Relationship(back_populates="user_permissions")  # type: ignore
    permission_id: int = Field(foreign_key="permission.id")
    permissions: list[Permission] = Relationship(back_populates="user_permissions")


class User(SQLModel, table=True):
    __tablename__: str = "user"

    id: int = Field(primary_key=True)
    login: EmailStr
    password: str
    is_client: bool = False
    is_manager: bool = False
    is_worker: bool = False

    profile_id: int = Field(foreign_key="profile.id")

    profile: Profile = Relationship(back_populates="user")
    addresses: list["Address"] = Relationship(back_populates="user")  # type: ignore
    user_permissions: UserPermissions = Relationship(back_populates="users")
