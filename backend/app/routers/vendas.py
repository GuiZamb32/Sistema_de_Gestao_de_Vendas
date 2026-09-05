from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.venda import VendaCreate, VendaResponse
from app.services.venda_service import (
    buscar_venda,
    criar_venda,
    listar_vendas,
)

router = APIRouter(
    prefix="/api/vendas",
    tags=["Vendas"]
)


@router.post(
    "",
    response_model=VendaResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_nova_venda(
    dados: VendaCreate,
    db: Session = Depends(get_db)
):
    return criar_venda(
        db,
        dados
    )


@router.get(
    "",
    response_model=list[VendaResponse]
)
def listar_todas_vendas(
    db: Session = Depends(get_db)
):
    return listar_vendas(db)


@router.get(
    "/{venda_id}",
    response_model=VendaResponse
)
def obter_venda(
    venda_id: int,
    db: Session = Depends(get_db)
):
    return buscar_venda(
        db,
        venda_id
    )