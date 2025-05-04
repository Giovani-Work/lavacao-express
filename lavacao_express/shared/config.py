import os
from dotenv import load_dotenv

load_dotenv()


DB_USER = str(os.getenv("DB_USER"))
DB_USER_PWD = str(os.getenv("DB_USER_PWD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_SCHEMA = str(os.getenv("DB_SCHEMA"))
