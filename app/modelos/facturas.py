from pydantic import computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import cliente
from datetime import datetime


#El decorador @property proviene de python y sirve para convertir un metodo de una clase en una propiedad de solo lectura
#validacion pydantic v2, @computed_field es un decorador que te permite definir propiedades o metodos que se calculan dinamicamente

#crear el modelo facturas (id, fecha, vr_total, cliente)
class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular(cantidad * vr_unitario) de todas las transacciones de la factura
        total_factura = 0.0
        transacciones_factura = getattr(self, "transacciones", None)

        if not transacciones_factura:
            return 0.0

        for transaccion in transacciones_factura:
            total_factura += transaccion.vr_unitario * transaccion.cantidad

        return total_factura


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(SQLModel):
    fecha: datetime | None = None


class FacturaLeer(FacturaBase):
    id: int
    cliente_id: int


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")

    transacciones: list["Transaccion"] = Relationship(back_populates="factura")