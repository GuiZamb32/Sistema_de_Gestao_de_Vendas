from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.produto import (
    ProdutoCreate,
    ProdutoResponse,
    ProdutoStatusUpdate,
    ProdutoUpdate,
)
from app.services import produto_service


router = APIRouter(
    prefix="/api/produtos",
    tags=["Produtos"]
)


@router.post(
    "",
    response_model=ProdutoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    return produto_service.criar_produto(db, produto)


@router.get(
    "",
    response_model=list[ProdutoResponse]
)
def listar_produtos(
    db: Session = Depends(get_db)
):
    return produto_service.listar_produtos(db)


@router.get(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    return produto_service.buscar_produto(db, produto_id)


@router.put(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def atualizar_produto(
    produto_id: int,
    produto: ProdutoUpdate,
    db: Session = Depends(get_db)
):
    return produto_service.atualizar_produto(
        db,
        produto_id,
        produto
    )


@router.patch(
    "/{produto_id}/status",
    response_model=ProdutoResponse
)
def alterar_status(
    produto_id: int,
    dados: ProdutoStatusUpdate,
    db: Session = Depends(get_db)
):
    return produto_service.alterar_status(
        db,
        produto_id,
        dados.ativo
    )