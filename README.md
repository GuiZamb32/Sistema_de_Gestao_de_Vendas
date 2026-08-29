# Sistema de Gestão de Vendas

Sistema de Gestão de Vendas desenvolvido como aplicação web, utilizando React com TypeScript no Frontend, Python com FastAPI no Backend e PostgreSQL como banco de dados.

O projeto tem como objetivo transformar os requisitos definidos no desafio acadêmico em uma aplicação funcional, desenvolvida de forma incremental.

---

##  Status do Projeto

**Desenvolvimento:** Em andamento

### Etapa 1 — Infraestrutura inicial

- [x] Criar estrutura do projeto
- [x] Configurar Backend com Python
- [x] Criar ambiente virtual
- [x] Instalar FastAPI
- [x] Configurar Uvicorn
- [x] Configurar SQLAlchemy
- [x] Configurar Psycopg
- [x] Configurar PostgreSQL
- [x] Criar banco `sistema_gestao_vendas`
- [x] Criar conexão Backend → PostgreSQL
- [x] Criar Models iniciais
- [x] Criar tabelas no PostgreSQL
- [x] Criar endpoint de Health Check
- [x] Testar conexão com o banco

### Etapa 2 — Gestão de Clientes

- [x] Criar Schema de Cliente
- [x] Criar Service de Cliente
- [x] Criar Router de Clientes
- [x] Implementar cadastro de cliente
- [x] Implementar listagem de clientes
- [x] Implementar consulta de cliente
- [x] Implementar edição de cliente
- [x] Implementar ativação/desativação
- [x] Implementar validação de e-mail
- [x] Implementar tratamento de e-mail duplicado
- [x] Testar endpoints através do Swagger
- [x] Confirmar persistência no PostgreSQL

### Próximas funcionalidades

- [ ] Criar CRUD de Produtos
- [ ] Implementar controle de Estoque
- [ ] Criar Frontend React + TypeScript
- [ ] Integrar Frontend e Backend
---

#  Arquitetura

A aplicação será dividida em três partes principais:

```text
┌─────────────────────────────┐
│       FRONTEND              │
│       React + TypeScript    │
│                             │
│       localhost:5173        │
└──────────────┬──────────────┘
               │
               │ HTTP / API
               ↓
┌─────────────────────────────┐
│        BACKEND              │
│        Python + FastAPI     │
│                             │
│        localhost:8000       │
└──────────────┬──────────────┘
               │
               │ SQLAlchemy
               ↓
┌─────────────────────────────┐
│       POSTGRESQL            │
│                             │
│    sistema_gestao_vendas    │
└─────────────────────────────┘
```

---

#  Tecnologias

## Frontend

- React
- TypeScript
- Vite
- Axios

## Backend

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Psycopg
- Pydantic
- Pydantic Settings

## Banco de Dados

- PostgreSQL

## Ferramentas

- Visual Studio Code
- Git
- GitHub
- pgAdmin 4

---

#  Estrutura Inicial do Projeto

Atualmente o projeto possui a seguinte estrutura:

```text
Sistema_de_Gestao_de_Vendas/
│
├── backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   │
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   │
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── connection.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── cliente.py
│   │   │   ├── produto.py
│   │   │   └── estoque.py
│   │   │
│   │   ├── routers/
│   │   │   └── __init__.py
│   │   │
│   │   ├── schemas/
│   │   │   └── __init__.py
│   │   │
│   │   └── services/
│   │       └── __init__.py
│   │
│   ├── .env
│   ├── requirements.txt
│   └── venv/
│
└── frontend/
```

> A pasta `frontend` será configurada posteriormente com React + TypeScript.

---

#  Configuração do Backend

## 1. Acessar a pasta Backend

No terminal do VS Code:

```powershell
cd backend
```

---

## 2. Criar o ambiente virtual

Como o comando `python` não estava disponível diretamente no Windows, foi utilizado o launcher `py`.

Verificar a versão instalada:

```powershell
py --version
```

Resultado utilizado no desenvolvimento:

```text
Python 3.13.3
```

Criar o ambiente virtual:

```powershell
py -m venv venv
```

---

## 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
venv\Scripts\activate
```

Quando ativado corretamente, o terminal apresenta:

```text
(venv) PS C:\Users\...\Sistema_de_Gestao_de_Vendas\backend>
```

---

#  Dependências do Backend

Foram instaladas as principais dependências:

```powershell
pip install fastapi uvicorn sqlalchemy psycopg[binary] pydantic-settings
```

Também foi instalada a validação de e-mail:

```powershell
pip install email-validator
```

As dependências foram registradas no arquivo:

```text
requirements.txt
```

Para gerar/atualizar o arquivo:

```powershell
pip freeze > requirements.txt
```

---

#  FastAPI

O Backend utiliza o FastAPI para criação da API REST.

O arquivo principal é:

```text
backend/app/main.py
```

A aplicação foi configurada inicialmente com:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
```

A aplicação recebe o nome:

```text
Sistema de Gestão de Vendas
```

e possui a versão:

```text
1.0.0
```

---

#  Executando o Backend

Com o ambiente virtual ativado:

```powershell
uvicorn app.main:app --reload
```

O servidor é executado em:

```text
http://127.0.0.1:8000
```

O parâmetro:

```text
--reload
```

permite que o Uvicorn reinicie automaticamente quando arquivos do projeto forem modificados.

---

#  Health Check

Foi criado um endpoint para verificar se a API está funcionando:

```text
GET /api/health
```

Acessando:

```text
http://localhost:8000/api/health
```

Resultado esperado:

```json
{
  "status": "ok"
}
```

---

#  Swagger

O FastAPI disponibiliza automaticamente uma documentação interativa da API.

A documentação pode ser acessada em:

```text
http://localhost:8000/docs
```

Também existe o OpenAPI em:

```text
http://localhost:8000/openapi.json
```

---

#  PostgreSQL

O banco utilizado pelo projeto é o PostgreSQL.

Foi criado o banco:

```text
sistema_gestao_vendas
```

A estrutura inicial é:

```text
PostgreSQL
│
└── sistema_gestao_vendas
    │
    └── public
        └── Tables
```

---

#  Variáveis de Ambiente

As informações de conexão com o banco não são colocadas diretamente no código.

Foi criado o arquivo:

```text
backend/.env
```

Estrutura:

```env
DATABASE_URL=postgresql+psycopg://postgres:SUA_SENHA@localhost:5432/sistema_gestao_vendas
```

Exemplo:

```env
DATABASE_URL=postgresql+psycopg://postgres:123456@localhost:5432/sistema_gestao_vendas
```

> **Importante:** o arquivo `.env` não deve ser enviado para o GitHub caso contenha a senha real do banco.

---

#  Configuração

O arquivo:

```text
backend/app/core/config.py
```

é responsável por carregar as configurações do ambiente.

Foi utilizado o `pydantic-settings` para leitura do `.env`.

Estrutura utilizada:

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
```

---

#  Conexão com o Banco

A conexão com o PostgreSQL é realizada através do SQLAlchemy.

Arquivo:

```text
backend/app/database/connection.py
```

Responsabilidades:

- criar o Engine;
- criar as sessões;
- disponibilizar a conexão para os endpoints;
- criar a classe Base dos Models.

Estrutura principal:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

---

#  Models

Os Models representam as tabelas do banco de dados.

Foram criados inicialmente três Models:

```text
Cliente
Produto
Estoque
```

---

##  Cliente

Arquivo:

```text
backend/app/models/cliente.py
```

Tabela:

```text
clientes
```

Campos:

```text
id
nome
email
telefone
ativo
criado_em
```

O campo `email` é único.

O campo `ativo` permite ativar ou desativar um cliente sem necessariamente excluir o registro.

---

#  Produto

Arquivo:

```text
backend/app/models/produto.py
```

Tabela:

```text
produtos
```

Campos:

```text
id
nome
descricao
preco
ativo
criado_em
```

O preço utiliza:

```text
Numeric(10, 2)
```

para representar valores monetários.

---

#  Estoque

Arquivo:

```text
backend/app/models/estoque.py
```

Tabela:

```text
estoque
```

Campos:

```text
id
produto_id
quantidade
atualizado_em
```

O campo:

```text
produto_id
```

possui uma chave estrangeira relacionada à tabela:

```text
produtos
```

Relação inicial:

```text
PRODUTO
   │
   │ 1
   │
   │ 1
   ↓
ESTOQUE
```

---

#  Registro dos Models

O arquivo:

```text
backend/app/models/__init__.py
```

centraliza os Models:

```python
from app.models.cliente import Cliente
from app.models.produto import Produto
from app.models.estoque import Estoque
```

Isso permite que os Models sejam carregados pelo SQLAlchemy antes da criação das tabelas.

---

#  Criação das Tabelas

Inicialmente foi utilizado:

```python
Base.metadata.create_all(bind=engine)
```

Essa instrução verifica os Models registrados e cria no PostgreSQL as tabelas que ainda não existem.

Resultado:

```text
sistema_gestao_vendas
│
└── public
    │
    ├── clientes
    ├── produtos
    └── estoque
```

As três tabelas foram criadas com sucesso no PostgreSQL.

---

#  Teste da Conexão

Foi criado um endpoint específico para verificar a conexão entre FastAPI e PostgreSQL:

```text
GET /api/health/database
```

URL:

```text
http://localhost:8000/api/health/database
```

Resultado obtido:

```json
{
  "status": "ok",
  "database": "conectado"
}
```

Esse teste confirmou a comunicação entre:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
Psycopg
   ↓
PostgreSQL
```

---

#  Resultado da Etapa 1

Ao final desta etapa, a infraestrutura básica do sistema está funcionando.

Temos:

```text
                    SISTEMA DE GESTÃO DE VENDAS

                              BACKEND
                                 │
                                 ▼
                           ┌───────────┐
                           │  FastAPI  │
                           └─────┬─────┘
                                 │
                                 ▼
                           ┌───────────┐
                           │ SQLAlchemy│
                           └─────┬─────┘
                                 │
                                 ▼
                           ┌───────────┐
                           │  Psycopg  │
                           └─────┬─────┘
                                 │
                                 ▼
                         ┌─────────────────┐
                         │   PostgreSQL    │
                         │                 │
                         │ sistema_gestao  │
                         │    _vendas      │
                         └─────────────────┘
```

A API está disponível em:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

Health Check:

```text
http://localhost:8000/api/health
```

Health Check do Banco:

```text
http://localhost:8000/api/health/database
```

---

#  Próximas Etapas

## Etapa 2 — Clientes

Implementar:

- Schema de Cliente
- Cadastro de cliente
- Listagem de clientes
- Consulta de cliente
- Edição de cliente
- Ativação/desativação
- Validação de e-mail
- Tratamento de erros
- Testes através do Swagger

Endpoints previstos:

```text
POST   /api/clientes
GET    /api/clientes
GET    /api/clientes/{id}
PUT    /api/clientes/{id}
PATCH  /api/clientes/{id}/status
```

---

## Etapa 3 — Produtos

Implementar:

- Cadastro de produtos
- Consulta de produtos
- Edição de produtos
- Ativação/desativação
- Validação de preço

---

## Etapa 4 — Estoque

Implementar:

- Entrada de estoque
- Saída de estoque
- Consulta de estoque
- Atualização de quantidade
- Validação para evitar estoque negativo

---

## Etapa 5 — Frontend

Criar aplicação utilizando:

```text
React
TypeScript
Vite
Axios
```

O Frontend será responsável pela interface visual do sistema e consumirá a API desenvolvida com FastAPI.

---

#  Segurança

As informações sensíveis devem ser armazenadas em variáveis de ambiente.

Não versionar:

```text
.env
venv/
__pycache__/
```

Recomenda-se utilizar um `.gitignore` na raiz do projeto.

---

#  Observações

Este projeto está sendo desenvolvido de forma incremental.

A infraestrutura foi criada primeiro para garantir que:

1. O Backend execute corretamente.
2. O PostgreSQL esteja acessível.
3. O SQLAlchemy consiga se comunicar com o banco.
4. Os Models sejam convertidos em tabelas.
5. A API esteja preparada para receber as próximas funcionalidades.

A implementação das funcionalidades do sistema será realizada gradualmente, começando pelo cadastro e gerenciamento de clientes.
