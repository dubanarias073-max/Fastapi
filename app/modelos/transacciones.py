from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

# crear el modelo transacciones (id, cantidad, vr_unitario, id_factura)
class TransaccionBase(SQLModel):
    cantidad: int = Field(default=0)
    vr_unitario: float = Field(default=0.0)


class TransaccionCrear(TransaccionBase):
    pass


class Transaccioneditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int | None = Field(default=None, foreign_key="factura.id")
