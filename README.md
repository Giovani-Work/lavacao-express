
# Lavacao Express - Sistema de Gerenciamento de Lava-Rápido

## Conteúdo
1. [Documentação em Português](#documentação-em-português)
   - [Visão Geral](#visão-geral)
   - [Configuração](#configuração)
   - [Estrutura](#estrutura)
2. [Documentação em Inglês](#documentation-in-english)
   - [Overview](#overview)
   - [Setup](#setup)
   - [Structure](#structure)
3. [Arquivos Técnicos](#arquivos-técnicos)
   - [Dockerfile](#dockerfile)
   - [docker-compose.yml](#docker-composeyml)
   - [Configurações](#configurações)

---

## Documentação em Português

### Visão Geral
Sistema backend para gerenciamento de lava-rápido com:
- Autenticação JWT
- Agendamento de serviços
- Gestão de usuários
- Controle de permissões

### Configuração
```bash
# 1. Clonar repositório
git clone https://github.com/seuusuario/lavacao-express.git
cd lavacao-express

# 2. Configurar ambiente
cp .env.example .env
# Editar o .env com suas credenciais

# 3. Iniciar com Docker
docker-compose up -d --build
```

### Estrutura do Projeto
```
lavacao-express/
├── backend/
│   └── lavacao_express/
│       ├── modules/
│       │   └── user/
│       │       ├── models/
│       │       ├── schemas/
│       │       ├── router/
│       │       └── services/
│       └── shared/
│           ├── config.py
│           ├── deps.py
│           └── utils.py
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Documentation in English

### Overview
Car wash management backend system with:
- JWT Authentication
- Service scheduling
- User management
- Permission control

### Setup
```bash
# 1. Clone repository
git clone https://github.com/yourusername/lavacao-express.git
cd lavacao-express

# 2. Setup environment
cp .env.example .env
# Edit .env with your credentials

# 3. Start with Docker
docker-compose up -d --build
```

### Project Structure
```
lavacao-express/
├── backend/
│   └── lavacao_express/
│       ├── modules/
│       │   └── user/
│       │       ├── models/
│       │       ├── schemas/
│       │       ├── router/
│       │       └── services/
│       └── shared/
│           ├── config.py
│           ├── deps.py
│           └── utils.py
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Arquivos Técnicos

### Dockerfile
```dockerfile
FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . .
EXPOSE 8080
CMD ["uvicorn", "backend.lavacao_express.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### docker-compose.yml
```yaml
version: '3.8'
services:
  app:
    build: .
    ports: ["8080:8080"]
    environment:
      - DB_HOST=db
      - DB_USER=${DB_USER}
      - DB_USER_PWD=${DB_USER_PWD}
      - DB_SCHEMA=${DB_SCHEMA}
      - SECRET_KEY=${SECRET_KEY}
    depends_on: [db]
    volumes: [".:/app"]
    command: bash -c "uvicorn backend.lavacao_express.main:app --host 0.0.0.0 --port 8080 --reload"

  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_ROOT_PASSWORD}
      - MYSQL_DATABASE=${DB_SCHEMA}
      - MYSQL_USER=${DB_USER}
      - MYSQL_PASSWORD=${DB_USER_PWD}
    ports: ["3306:3306"]
    volumes: [mysql_data:/var/lib/mysql]
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 10s
      retries: 5

volumes:
  mysql_data:
```

### Configurações
`.env.example`
```ini
DB_HOST=db
DB_SCHEMA=lavacao_express
DB_USER=app_user
DB_USER_PWD=strongpassword
DB_ROOT_PASSWORD=rootpassword
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=120
REFRESH_TOKEN_EXPIRE_MINUTES=240
```

---

**Contato**: Giovani Liskoski Zanini - [giovanilzanini@hotmail.com](mailto:giovanilzanini@hotmail.com)  
**Licença**: GNU GPL v3.0
