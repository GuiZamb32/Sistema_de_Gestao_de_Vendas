from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.models.produto import Produto


def buscar_estoque_por_produto(
    db: Session,
    produto_id: int
):
    estoque = (
        db.query(Estoque)
        .filter(Estoque.produto_id == produto_id)
        .first()
    )

    if not estoque:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estoque do produto não encontrado."
        )

    return estoque


def criar_estoque(
    db: Session,
    produto_id: int,
    quantidade: int = 0
):
    produto = (
        db.query(Produto)
        .filter(Produto.id == produto_id)
        .first()
    )

    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado."
        )

    estoque_existente = (
        db.query(Estoque)
        .filter(Estoque.produto_id == produto_id)
        .first()
    )

    if estoque_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Este produto já possui um estoque cadastrado."
        )

    estoque = Estoque(
        produto_id=produto_id,
        quantidade=quantidade
    )

    db.add(estoque)
    db.commit()
    db.refresh(estoque)

    return estoque


def adicionar_estoque(
    db: Session,
    produto_id: int,
    quantidade: int
):
    if quantidade <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A quantidade de entrada deve ser maior que zero."
        )

    estoque = buscar_estoque_por_produto(
        db,
        produto_id
    )

    estoque.quantidade += quantidade

    db.commit()
    db.refresh(estoque)

    return estoque


def retirar_estoque(
    db: Session,
    produto_id: int,
    quantidade: int
):
    if quantidade <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A quantidade de saída deve ser maior que zero."
        )

    estoque = buscar_estoque_por_produto(
        db,
        produto_id
    )

    if estoque.quantidade < quantidade:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantidade solicitada maior que o estoque disponível."
        )

    estoque.quantidade -= quantidade

    db.commit()
    db.refresh(estoque)

    return estoque


def atualizar_estoque(
    db: Session,
    produto_id: int,
    quantidade: int
):
    if quantidade < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A quantidade não pode ser negativa."
        )

    estoque = buscar_estoque_por_produto(
        db,
        produto_id
    )

    estoque.quantidade = quantidade

    db.commit()
    db.refresh(estoque)

    return estoque