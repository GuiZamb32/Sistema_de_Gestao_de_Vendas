from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EstoqueBase(BaseModel):
    quantidade: int = Field(
        default=0,
        ge=0,
        description="Quantidade atual disponível em estoque"
    )


class EstoqueEntrada(BaseModel):
    quantidade: int = Field(
        ...,
        gt=0,
        description="Quantidade de produtos adicionada ao estoque"
    )


class EstoqueSaida(BaseModel):
    quantidade: int = Field(
        ...,
        gt=0,
        description="Quantidade de produtos retirada do estoque"
    )


class EstoqueResponse(EstoqueBase):
    id: int
    produto_id: int
    atualizado_em: datetime

    model_config = ConfigDict(from_attributes=True)