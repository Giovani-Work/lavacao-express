import os
from fastapi import FastAPI
import uvicorn
from lavacao_express.modules.user.router import account

# for path, subpath, files in os.walk("./lava")

app = FastAPI()
app.include_router(account.router, prefix="/api/account")


if __name__ == "__main__":
    uvicorn.run(app=app, port=8080)
