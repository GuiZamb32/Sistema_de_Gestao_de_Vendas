from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate


def criar_produto(
    db: Session,
    produto: ProdutoCreate
):

    novo_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return buscar_produto(
        db,
        novo_produto.id
    )


def listar_produtos(db: Session):

    produtos = (
        db.query(Produto)
        .order_by(Produto.id)
        .all()
    )

    resultado = []

    for produto in produtos:
        estoque = (
            db.query(Estoque)
            .filter(Estoque.produto_id == produto.id)
            .first()
        )

        resultado.append({
            "id": produto.id,
            "nome": produto.nome,
            "descricao": produto.descricao,
            "preco": produto.preco,
            "ativo": produto.ativo,
            "criado_em": produto.criado_em,
            "atualizado_em": produto.atualizado_em,
            "estoque_quantidade": (
                estoque.quantidade
                if estoque
                else 0
            ),
        })

    return resultado


def buscar_produto(
    db: Session,
    produto_id: int
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

    estoque = (
        db.query(Estoque)
        .filter(Estoque.produto_id == produto.id)
        .first()
    )

    return {
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "preco": produto.preco,
        "ativo": produto.ativo,
        "criado_em": produto.criado_em,
        "atualizado_em": produto.atualizado_em,
        "estoque_quantidade": (
            estoque.quantidade
            if estoque
            else 0
        ),
    }


def atualizar_produto(
    db: Session,
    produto_id: int,
    dados: ProdutoUpdate
):

    produto = buscar_produto_modelo(
        db,
        produto_id
    )

    produto.nome = dados.nome
    produto.descricao = dados.descricao
    produto.preco = dados.preco

    db.commit()
    db.refresh(produto)

    return buscar_produto(
        db,
        produto_id
    )


def alterar_status(
    db: Session,
    produto_id: int,
    ativo: bool
):

    produto = buscar_produto_modelo(
        db,
        produto_id
    )

    produto.ativo = ativo

    db.commit()
    db.refresh(produto)

    return buscar_produto(
        db,
        produto_id
    )


def buscar_produto_modelo(
    db: Session,
    produto_id: int
) -> Produto:

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