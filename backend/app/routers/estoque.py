from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.estoque import (
    EstoqueEntrada,
    EstoqueResponse,
    EstoqueSaida,
)
from app.services.estoque_service import (
    adicionar_estoque,
    atualizar_estoque,
    buscar_estoque_por_produto,
    criar_estoque,
    retirar_estoque,
)

router = APIRouter(
    prefix="/api/estoque",
    tags=["Estoque"]
)


@router.get(
    "/{produto_id}",
    response_model=EstoqueResponse
)
def obter_estoque(
    produto_id: int,
    db: Session = Depends(get_db)
):
    return buscar_estoque_por_produto(
        db,
        produto_id
    )


@router.post(
    "/{produto_id}",
    response_model=EstoqueResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_estoque_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    return criar_estoque(
        db,
        produto_id
    )


@router.post(
    "/{produto_id}/entrada",
    response_model=EstoqueResponse
)
def entrada_estoque(
    produto_id: int,
    dados: EstoqueEntrada,
    db: Session = Depends(get_db)
):
    return adicionar_estoque(
        db,
        produto_id,
        dados.quantidade
    )


@router.post(
    "/{produto_id}/saida",
    response_model=EstoqueResponse
)
def saida_estoque(
    produto_id: int,
    dados: EstoqueSaida,
    db: Session = Depends(get_db)
):
    return retirar_estoque(
        db,
        produto_id,
        dados.quantidade
    )


@router.put(
    "/{produto_id}",
    response_model=EstoqueResponse
)
def atualizar_estoque_produto(
    produto_id: int,
    dados: EstoqueEntrada,
    db: Session = Depends(get_db)
):
    return atualizar_estoque(
        db,
        produto_id,
        dados.quantidade
    )