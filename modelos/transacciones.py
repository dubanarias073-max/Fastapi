from pydantic import BaseModel

#crear el modelo transaccion( id, cantidad, vr _unitario, id_factura)
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    id_factura: int

class TransaccionCrear(TransaccionBase):
    id: int | None = None
    #aqui va la relacion co el modelo cliente (solo un campo)