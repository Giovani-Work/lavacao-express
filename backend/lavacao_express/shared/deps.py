from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import create_engine, Session

from lavacao_express.shared import config


engine = create_engine(
    f"mysql+pymysql://{config.DB_USER}:{config.DB_USER_PWD}@{config.DB_HOST}/{config.DB_SCHEMA}"
)


def session() -> Generator[Session, None, None]:
    with Session(engine) as _session:
        yield _session


DbSession = Annotated[Session, Depends(session)]
