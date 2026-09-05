from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.models.estoque import Estoque
from app.models.item_venda import ItemVenda
from app.models.produto import Produto
from app.models.venda import Venda
from app.schemas.venda import VendaCreate


def criar_venda(
    db: Session,
    dados: VendaCreate
):
    cliente = (
        db.query(Cliente)
        .filter(Cliente.id == dados.cliente_id)
        .first()
    )

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado."
        )

    venda = Venda(
        cliente_id=dados.cliente_id,
        valor_total=0,
        status="finalizada"
    )

    db.add(venda)

    valor_total = 0

    for item in dados.itens:
        produto = (
            db.query(Produto)
            .filter(Produto.id == item.produto_id)
            .first()
        )

        if not produto:
            db.rollback()

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Produto {item.produto_id} não encontrado."
            )

        if not produto.ativo:
            db.rollback()

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"O produto '{produto.nome}' está inativo."
            )

        estoque = (
            db.query(Estoque)
            .filter(Estoque.produto_id == item.produto_id)
            .first()
        )

        if not estoque:
            db.rollback()

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estoque do produto '{produto.nome}' não encontrado."
            )

        if estoque.quantidade < item.quantidade:
            db.rollback()

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    f"Estoque insuficiente para o produto "
                    f"'{produto.nome}'. Disponível: "
                    f"{estoque.quantidade}."
                )
            )

        subtotal = produto.preco * item.quantidade

        item_venda = ItemVenda(
            venda=venda,
            produto_id=produto.id,
            quantidade=item.quantidade,
            preco_unitario=produto.preco,
            subtotal=subtotal
        )

        db.add(item_venda)

        estoque.quantidade -= item.quantidade

        valor_total += subtotal

    venda.valor_total = valor_total

    db.commit()
    db.refresh(venda)

    return venda


def buscar_venda(
    db: Session,
    venda_id: int
):
    venda = (
        db.query(Venda)
        .filter(Venda.id == venda_id)
        .first()
    )

    if not venda:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venda não encontrada."
        )

    return venda


def listar_vendas(
    db: Session
):
    return (
        db.query(Venda)
        .order_by(Venda.id.desc())
        .all()
    )