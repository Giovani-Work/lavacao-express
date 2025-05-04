from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session
from lavacao_express.shared import config


engine = create_engine(
    f"mysql+pymysql://{config.DB_USER}:{config.DB_USER_PWD}@{config.DB_HOST}/{config.DB_SCHEMA}"
)
# SQLModel.metadata.create_all(engine)


def session() -> Generator[Session, None, None]:
    with Session(engine) as _session:
        yield _session

def sum_sum_n(x, y):
    return x + y


DbSession = Annotated[Session, Depends(session)]

