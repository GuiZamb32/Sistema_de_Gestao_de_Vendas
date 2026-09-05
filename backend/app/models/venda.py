from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.connection import Base


class Venda(Base):
    __tablename__ = "vendas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    valor_total = Column(
        Numeric(10, 2),
        nullable=False,
        default=0
    )

    status = Column(
        String(20),
        nullable=False,
        default="finalizada"
    )

    criado_em = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    cliente = relationship(
        "Cliente",
        backref="vendas"
    )

    itens = relationship(
        "ItemVenda",
        back_populates="venda",
        cascade="all, delete-orphan"
    )