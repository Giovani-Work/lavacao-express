import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

load_dotenv()


DB_USER = str(os.getenv("DB_USER"))
DB_USER_PWD = str(os.getenv("DB_USER_PWD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_SCHEMA = str(os.getenv("DB_SCHEMA"))

# Configurações (coloque em variáveis de ambiente na produção)
SECRET_KEY = "sua-chave-secreta-super-segura-aqui"  # Troque por uma chave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120
REFRESH_TOKEN_EXPIRE_MINUTES = 240

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
