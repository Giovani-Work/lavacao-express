from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Profile(SQLModel, table=True):
    __tablename__ = "profile"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    cpf: str = Field(max_length=11)
    email: str = Field(max_length=320)
    cell_phone: Optional[str] = Field(max_length=15, default=None)
    photo: Optional[str] = Field(max_length=50, default=None)

    users: List["User"] = Relationship(back_populates="profile")


class Address(SQLModel, table=True):
    __tablename__ = "address"

    id: Optional[int] = Field(default=None, primary_key=True)
    street: str = Field(max_length=200)
    number: str = Field(max_length=25)
    district: Optional[str] = Field(max_length=100, default=None)
    city: Optional[str] = Field(max_length=100, default=None)
    state: Optional[str] = Field(max_length=100, default=None)
    postal_code: str = Field(max_length=45)
    is_principal: bool = Field(default=False)

    users: List["User"] = Relationship(back_populates="address")
    user_id: int = Field(foreign_key="user.id")


class Permission(SQLModel, table=True):
    __tablename__ = "permission"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(max_length=50, default=None)
    is_active: Optional[bool] = Field(default=None)

    user_permissions: List["UserPermissions"] = Relationship(
        back_populates="permission"
    )


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    login: str = Field(max_length=100, unique=True)
    password: str = Field(max_length=64)
    profile_id: int = Field(foreign_key="profile.id")
    # address_id: int = Field(foreign_key="address.id")
    is_client: bool = Field(default=False)
    is_manager: bool = Field(default=False)
    is_worker: bool = Field(default=False)

    profile: Profile = Relationship(back_populates="users")
    address: Address = Relationship(back_populates="users")
    user_permissions: List["UserPermissions"] = Relationship(back_populates="user")


class UserPermissions(SQLModel, table=True):
    __tablename__ = "user_permissions"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    permissions_id: int = Field(foreign_key="permission.id")

    user: User = Relationship(back_populates="user_permissions")
    permission: Permission = Relationship(back_populates="user_permissions")
