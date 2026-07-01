from __future__ import annotations

from pydantic import BaseModel

# crear el modelo transacciones (id, cantidad, vr_unitario, id_factura)
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float


class TransaccionCrear(TransaccionBase):
    pass


class Transaccioneditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase):
    id: int | None = None
    factura_id: int | None = None
    factura_id: int | None = None
        