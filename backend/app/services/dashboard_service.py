from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.models.estoque import Estoque
from app.models.produto import Produto
from app.models.item_venda import ItemVenda
from app.models.venda import Venda


def obter_resumo_dashboard(db: Session):
    total_vendas = (
        db.query(func.count(Venda.id))
        .scalar()
    )

    faturamento_total = (
        db.query(func.coalesce(func.sum(Venda.valor_total), 0))
        .filter(Venda.status == "finalizada")
        .scalar()
    )

    total_produtos = (
        db.query(func.count(Produto.id))
        .filter(Produto.ativo == True)
        .scalar()
    )

    total_clientes = (
        db.query(func.count(Cliente.id))
        .filter(Cliente.ativo == True)
        .scalar()
    )

    produtos_estoque_baixo = (
        db.query(func.count(Estoque.id))
        .filter(Estoque.quantidade <= 5)
        .scalar()
    )

    vendas_recentes = (
        db.query(Venda)
        .order_by(Venda.criado_em.desc())
        .limit(5)
        .all()
    )

    produtos_mais_vendidos = (
        db.query(
            Produto.id.label("produto_id"),
            Produto.nome.label("nome"),
            func.sum(ItemVenda.quantidade).label("quantidade_vendida")
        )
        .join(ItemVenda, ItemVenda.produto_id == Produto.id)
        .join(Venda, Venda.id == ItemVenda.venda_id)
        .filter(Venda.status == "finalizada")
        .group_by(Produto.id, Produto.nome)
        .order_by(func.sum(ItemVenda.quantidade).desc())
        .limit(5)
        .all()
    )

    return {
        "total_vendas": total_vendas or 0,
        "faturamento_total": faturamento_total or 0,
        "total_produtos": total_produtos or 0,
        "total_clientes": total_clientes or 0,
        "produtos_estoque_baixo": produtos_estoque_baixo or 0,
        "vendas_recentes": vendas_recentes,
        "produtos_mais_vendidos": produtos_mais_vendidos,
    }