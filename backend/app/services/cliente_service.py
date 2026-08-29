from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate


def criar_cliente(db: Session, dados: ClienteCreate) -> Cliente:
    cliente_existente = db.scalar(
        select(Cliente).where(Cliente.email == dados.email)
    )

    if cliente_existente:
        raise ValueError("Já existe um cliente cadastrado com este e-mail.")

    cliente = Cliente(
        nome=dados.nome,
        email=dados.email,
        telefone=dados.telefone,
    )

    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    return cliente


def listar_clientes(db: Session) -> list[Cliente]:
    return list(
        db.scalars(
            select(Cliente).order_by(Cliente.id)
        ).all()
    )


def buscar_cliente(db: Session, cliente_id: int) -> Cliente | None:
    return db.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )


def atualizar_cliente(
    db: Session,
    cliente: Cliente,
    dados: ClienteUpdate,
) -> Cliente:

    if dados.email is not None and dados.email != cliente.email:
        cliente_existente = db.scalar(
            select(Cliente).where(
                Cliente.email == dados.email,
                Cliente.id != cliente.id,
            )
        )

        if cliente_existente:
            raise ValueError(
                "Já existe outro cliente cadastrado com este e-mail."
            )

    if dados.nome is not None:
        cliente.nome = dados.nome

    if dados.email is not None:
        cliente.email = dados.email

    if dados.telefone is not None:
        cliente.telefone = dados.telefone

    db.commit()
    db.refresh(cliente)

    return cliente


def alterar_status(
    db: Session,
    cliente: Cliente,
    ativo: bool,
) -> Cliente:

    cliente.ativo = ativo

    db.commit()
    db.refresh(cliente)

    return cliente