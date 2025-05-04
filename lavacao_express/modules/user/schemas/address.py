from pydantic import BaseModel, Field


class WriteAddress(BaseModel):
    street: str
    number: str
    district: str
    city: str
    state: str
    postal_code: str = Field(regex=r"")
    is_princiapl: bool
