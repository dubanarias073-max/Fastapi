from pydantic import BaseModel, computed_field, Field

from .transacciones import Transaccion
from .clientes import cliente
from datetime import datetime

#El decorador @property proviene de python y sirve para convertir un metodo de una clase en una propiedad de solo lectura
#validacion pydantic v2, @computed_field es un decorador que te permite definir propiedades o metodos que se calculan dinamicamente
#getattr() es una funcion nativa de python. sirve para obtener el valor de un atributo o propiedad de un objeto de forma dinamica.

#crear el modelo facturas (id, fecha, vr_total, cliente)
class FacturaBase(BaseModel):
    fecha: datetime = datetime.now()
    cliente: cliente
    transacciones: list[Transaccion] = Field(default_factory=list)

    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular(cantidad * vr_unitario)

        #consultar el id actual de la factura
        factura_id_actual = getattr(self, "id", None)

        total_factura = 0.0

        if not factura_id_actual or not self.transacciones:
            return 0.0

        #recorrer la lista de transacciones segun el factura_id
        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad

        return total_factura

class FacturaCrear(FacturaBase):
    pass

class Facturaeditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id :int | None = None