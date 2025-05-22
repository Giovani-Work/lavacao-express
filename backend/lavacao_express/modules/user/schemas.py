from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class WriteAddress(BaseModel):
    street: str
    number: str
    district: str
    city: str
    state: str
    postal_code: str
    is_principal: bool


class ReadAddress(BaseModel):
    id: int
    street: str
    number: str
    district: str
    city: str
    state: str
    postal_code: str
    is_principal: bool


class WriteProfile(BaseModel):
    first_name: str
    last_name: str
    cpf: str
    email: EmailStr
    cell_phone: PhoneNumber | None = None
    photo: str | None = None


class ReadProfile(BaseModel):
    id: int
    first_name: str
    last_name: str
    cpf: str
    email: EmailStr
    cell_phone: PhoneNumber | None = None
    photo: str | None = None


class WriteUser(BaseModel):
    password: str
    profile: WriteProfile
    address: list[WriteAddress]


class ReadUser(BaseModel):
    id: int
    profile: ReadProfile
    address: list[ReadAddress]


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserLogin(BaseModel):
    login: str
    password: str


class UserLogged(BaseModel):
    id: int
    login: str
    profile: ReadProfile
    access_token: Token
    refresh_token: Token
