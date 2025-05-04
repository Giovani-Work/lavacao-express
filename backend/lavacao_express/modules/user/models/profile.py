from fastapi import Path
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class Profile(SQLModel, table=True):
    __tablename__: str = "profile"

    id: int = Field(primary_key=True)
    first_name: str
    last_name: str
    cpf: str
    email: EmailStr
    cell_phone: PhoneNumber | None = Field(default=None)
    photo: str | None = Field(default=None)

    user: "User" = Relationship(back_populates="profile")  # type: ignore
