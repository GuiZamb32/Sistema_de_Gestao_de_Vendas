from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class VendaRecente(BaseModel):
    id: int
    cliente_id: int
    valor_total: Decimal
    status: str
    criado_em: datetime


class ProdutoMaisVendido(BaseModel):
    produto_id: int
    nome: str
    quantidade_vendida: int


class DashboardResumo(BaseModel):
    total_vendas: int
    faturamento_total: Decimal
    total_produtos: int
    total_clientes: int
    produtos_estoque_baixo: int
    vendas_recentes: list[VendaRecente]
    produtos_mais_vendidos: list[ProdutoMaisVendido]