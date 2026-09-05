from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database.connection import Base, engine
from app.models import Cliente, Produto, Estoque, Venda, ItemVenda

from app.routers.clientes import router as clientes_router
from app.routers.produtos import router as produtos_router
from app.routers.estoque import router as estoque_router
from app.routers.vendas import router as vendas_router


app = FastAPI(
    title="Sistema de Gestão de Vendas",
    description="API do Sistema de Gestão de Vendas",
    version="1.0.0"
)


Base.metadata.create_all(bind=engine)
app.include_router(clientes_router)
app.include_router(produtos_router)
app.include_router(estoque_router)
app.include_router(vendas_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "API do Sistema de Gestão de Vendas funcionando!"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/api/health/database")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "database": "conectado"
        }

    except Exception as error:
        return {
            "status": "error",
            "database": "não conectado",
            "detail": str(error)
        }