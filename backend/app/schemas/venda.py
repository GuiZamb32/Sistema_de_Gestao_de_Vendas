from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ItemVendaCreate(BaseModel):
    produto_id: int = Field(
        ...,
        gt=0,
        description="ID do produto vendido"
    )

    quantidade: int = Field(
        ...,
        gt=0,
        description="Quantidade do produto"
    )


class VendaCreate(BaseModel):
    cliente_id: int = Field(
        ...,
        gt=0,
        description="ID do cliente responsável pela venda"
    )

    itens: list[ItemVendaCreate] = Field(
        ...,
        min_length=1,
        description="Produtos que fazem parte da venda"
    )


class ItemVendaResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    preco_unitario: Decimal
    subtotal: Decimal

    model_config = ConfigDict(
        from_attributes=True
    )


class VendaResponse(BaseModel):
    id: int
    cliente_id: int
    valor_total: Decimal
    status: str
    criado_em: datetime
    itens: list[ItemVendaResponse]

    model_config = ConfigDict(
        from_attributes=True
    )