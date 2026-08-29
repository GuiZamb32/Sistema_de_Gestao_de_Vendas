from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=2, max_length=150)
    descricao: str | None = Field(default=None, max_length=500)
    preco: Decimal = Field(..., gt=0, decimal_places=2)


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(ProdutoBase):
    pass


class ProdutoStatusUpdate(BaseModel):
    ativo: bool


class ProdutoResponse(ProdutoBase):
    id: int
    ativo: bool
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)