# python-api

API desenvolvida com FastAPI para revisão e prática de estudo de Python. Essa API simples retorna instituições financeiras contando com um stream de eventos em tempo real (Server-Sent Events) que emite o horário atual. O projeto utiliza SQLAlchemy como ORM, Alembic para controle de migrações do banco de dados, e Pydantic Settings para gerenciamento de configurações via variáveis de ambiente.

## Stack Tecnológica

- **FastAPI** — framework web assíncrono para construção da API
- **Uvicorn** — servidor ASGI utilizado para rodar a aplicação
- **SQLAlchemy** — ORM para modelagem e acesso ao banco de dados
- **Alembic** — ferramenta de migrações de banco de dados
- **Pydantic Settings** — carregamento e validação de configurações via variáveis de ambiente
- **passlib[bcrypt]** e **python-jose[cryptography]** — utilizados para autenticação e hashing de senhas
- **sse-starlette** — implementação de Server-Sent Events (SSE)
- **tzlocal** — detecção automática do fuso horário local
- **SQLite** — banco de dados padrão do projeto (configurável via `DATABASE_URL`)

## Estrutura do Projeto

```
app/
├── main.py              # Ponto de entrada da aplicação FastAPI
├── config.py             # Configurações (variáveis de ambiente)
├── database.py            # Engine e sessão do SQLAlchemy
└── api/v1/
    ├── endpoints.py       # Agrega todas as rotas da versão v1
    ├── banks/
    │   ├── router.py       # Rotas de /api/v1/banks
    │   ├── schemas.py      # Schemas Pydantic (validação de entrada/saída)
    │   ├── models.py       # Modelos SQLAlchemy (tabelas do banco)
    │   └── services.py     # Lógica de acesso ao banco de dados
    └── clock/
        ├── router.py       # Rotas de /api/v1/clock (SSE)
        └── services.py     # Gerador do stream de eventos
alembic/                  # Migrações do banco de dados
```

## Configuração e Instalação

1. Crie um ambiente virtual e instale as dependências:
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   PROJECT_NAME=python-api
   DATABASE_URL=sqlite:///./sql_app.db
   ```

3. Execute as migrações do banco de dados:
   ```
   alembic upgrade head
   ```

4. Inicie o servidor:
   ```
   uvicorn app.main:app --reload
   ```

A documentação interativa da API (Swagger) fica disponível em `http://localhost:8000/docs`.

## Endpoints

| Método | Rota                         | Descrição                                          |
|--------|------------------------------|-----------------------------------------------------|
| GET    | `/`                          | Verificação de saúde da aplicação (health check)     |
| GET    | `/api/v1/banks/`             | Lista todas as instituições financeiras cadastradas  |
| POST   | `/api/v1/banks/`             | Cadastra uma nova instituição financeira             |
| GET    | `/api/v1/banks/{tax_id}`  | Busca uma instituição financeira pelo CNPJ           |
| PUT    | `/api/v1/banks/{id}`         | Atualiza parcialmente uma instituição financeira pelo id |
| DELETE | `/api/v1/banks/{id}`         | Remove uma instituição financeira pelo id            |
| GET    | `/api/v1/clock/stream`       | Stream SSE com fuso horário e timestamp atualizados  |

## Schema de Banco (Instituição Financeira)

- `taxId` (str) — CNPJ da instituição (coluna `tax_id`)
- `name` (str) — Nome do banco
- `fantasyName` (str) — Nome fantasia da instituição (coluna `fantasy_name`)
- `ispb` (str, opcional) — Identificador do Sistema de Pagamentos Brasileiro
- `compeCode` (str) — Código do Sistema de Compensação de Cheques e Outros Papéis (coluna `compe_code`)

No `PUT`, todos os campos são opcionais (`BanksUpdate`) — apenas os campos enviados são atualizados.

> Nota: `GET /api/v1/banks/{tax_id}` busca pelo campo `taxId` (coluna `tax_id`), apesar do nome do parâmetro na rota.
