from sqlmodel import Relationship, SQLModel, Field

from lavacao_express.modules.user.models.user import User


class Address(SQLModel, table=True):
    __tablename__: str = "address"

    id: int = Field(primary_key=True)
    street: str
    number: str
    district: str | None = Field(default=None)
    city: str | None = Field(default=None)
    state: str | None = Field(default=None)
    postal_code: str = Field(default=None)
    is_princiapl: bool

    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="addresses")
