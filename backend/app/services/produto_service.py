from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate


def criar_produto(db: Session, produto: ProdutoCreate) -> Produto:
    novo_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


def listar_produtos(db: Session) -> list[Produto]:
    return db.query(Produto).order_by(Produto.id).all()


def buscar_produto(db: Session, produto_id: int) -> Produto:
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

    return produto


def atualizar_produto(
    db: Session,
    produto_id: int,
    dados: ProdutoUpdate
) -> Produto:

    produto = buscar_produto(db, produto_id)

    produto.nome = dados.nome
    produto.descricao = dados.descricao
    produto.preco = dados.preco

    db.commit()
    db.refresh(produto)

    return produto


def alterar_status(
    db: Session,
    produto_id: int,
    ativo: bool
) -> Produto:

    produto = buscar_produto(db, produto_id)

    produto.ativo = ativo

    db.commit()
    db.refresh(produto)

    return produto