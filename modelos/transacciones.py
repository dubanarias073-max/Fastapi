from pydantic import BaseModel

# Modelo base con los atributos comunes
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    id_factura: int

# Modelo utilizado para recibir datos al crear una transacción
class TransaccionCrear(TransaccionBase):
    pass

# Modelo utilizado para actualizaciones parciales (PATCH)
# Se vuelven todos los campos opcionales para permitir modificar solo lo necesario
class Transaccioneditar(BaseModel):
    cantidad: int | None = None
    vr_unitario: float | None = None
    id_factura: int | None = None

# Modelo completo que representa la estructura final en la lista
class Transaccion(TransaccionBase):
    id: int
    id_cliente: int  