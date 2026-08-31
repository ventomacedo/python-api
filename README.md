# python-api

FastAPI service for managing Brazilian financial institutions (banks), with a Server-Sent Events clock stream. Uses SQLAlchemy for ORM, Alembic for migrations, and Pydantic Settings for config.

## Tech Stack

- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic (migrations)
- Pydantic Settings
- passlib[bcrypt], python-jose[cryptography] (auth)
- sse-starlette (Server-Sent Events)
- tzlocal (local timezone detection)
- SQLite (default, via `DATABASE_URL`)

## Project Structure

```
app/
├── main.py              # FastAPI app entrypoint
├── config.py            # Settings (env vars)
├── database.py          # SQLAlchemy engine/session
└── api/v1/
    ├── endpoints.py      # Aggregates all v1 routers
    ├── banks/
    │   ├── router.py      # /api/v1/banks routes
    │   ├── schemas.py     # Pydantic schemas
    │   ├── models.py      # SQLAlchemy models
    │   └── services.py    # DB access logic
    └── clock/
        ├── router.py      # /api/v1/clock routes (SSE)
        └── services.py    # Event stream generator
alembic/                 # Migrations
```

## Setup

1. Create virtualenv and install deps:
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Create `.env` in project root:
   ```
   PROJECT_NAME=python-api
   DATABASE_URL=sqlite:///./sql_app.db
   ```

3. Run migrations:
   ```
   alembic upgrade head
   ```

4. Start server:
   ```
   uvicorn app.main:app --reload
   ```

API docs available at `http://localhost:8000/docs`.

## Endpoints

| Method | Path                        | Description                     |
|--------|-----------------------------|----------------------------------|
| GET    | `/`                         | Health check                     |
| GET    | `/api/v1/banks/`            | List banks                       |
| POST   | `/api/v1/banks/`            | Create bank                      |
| GET    | `/api/v1/banks/{bank_cnpj}` | Get bank by CNPJ                 |
| GET    | `/api/v1/clock/stream`      | SSE stream of timezone/timestamp |

## Bank Schema

- `cnpj` (str) — CNPJ da instituição
- `name` (str) — Nome do banco
- `fantasy_name` (str) — Nome fantasia da instituição
- `ispb` (str, optional) — Identificador do Sistema de Pagamento Brasileiro
- `compe_code` (str) — Código do Sistema de Compensação de Cheques e Outros Papeis
