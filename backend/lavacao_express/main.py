from contextlib import asynccontextmanager
import json
import os
from fastapi import FastAPI
from sqlmodel import Session
import uvicorn

# from backend.lavacao_express.modules.user.models.permissions import Permission
from backend.lavacao_express.modules.user.models import Permission
from backend.lavacao_express.modules.user.router import account, auth
from backend.lavacao_express.shared.deps import engine

# from lavacao_express.modules.user.router import account


@asynccontextmanager
async def lifesplan(app: FastAPI):
    with open("base-parmission.json", "r") as file:
        base_authorization = json.load(file)
    _session = Session(engine)
    for permission in base_authorization["permissions"]:
        _session.add(Permission(name=permission, is_active=True))
    _session.commit()
    for group in base_authorization["groups"]:
        

    yield
    _session.close()


app = FastAPI(lifespan=lifesplan)
app.include_router(account.router, prefix="/api/account")
app.include_router(auth.router, prefix="/api/auth")


if __name__ == "__main__":
    uvicorn.run(app=app, port=8080)
