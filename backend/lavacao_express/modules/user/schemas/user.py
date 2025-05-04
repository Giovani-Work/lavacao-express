from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class WriteUser(BaseModel):
    password: str
    first_name: str
    last_name: str
    cpf: str
    email: EmailStr
    cell_phone: PhoneNumber | None = None
    photo: str | None = None
