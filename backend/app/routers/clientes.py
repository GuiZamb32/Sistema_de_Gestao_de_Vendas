from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.cliente import ClienteCreate, ClienteResponse, ClienteUpdate
from app.services import cliente_service


router = APIRouter(
    prefix="/api/clientes",
    tags=["Clientes"],
)


@router.post(
    "",
    response_model=ClienteResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_cliente(
    dados: ClienteCreate,
    db: Session = Depends(get_db),
):
    try:
        return cliente_service.criar_cliente(db, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro),
        )


@router.get(
    "",
    response_model=list[ClienteResponse],
)
def listar_clientes(
    db: Session = Depends(get_db),
):
    return cliente_service.listar_clientes(db)


@router.get(
    "/{cliente_id}",
    response_model=ClienteResponse,
)
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
):
    cliente = cliente_service.buscar_cliente(db, cliente_id)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado.",
        )

    return cliente


@router.put(
    "/{cliente_id}",
    response_model=ClienteResponse,
)
def atualizar_cliente(
    cliente_id: int,
    dados: ClienteUpdate,
    db: Session = Depends(get_db),
):
    cliente = cliente_service.buscar_cliente(db, cliente_id)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado.",
        )

    try:
        return cliente_service.atualizar_cliente(
            db,
            cliente,
            dados,
        )

    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro),
        )


@router.patch(
    "/{cliente_id}/status",
    response_model=ClienteResponse,
)
def alterar_status(
    cliente_id: int,
    ativo: bool,
    db: Session = Depends(get_db),
):
    cliente = cliente_service.buscar_cliente(db, cliente_id)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado.",
        )

    return cliente_service.alterar_status(
        db,
        cliente,
        ativo,
    )