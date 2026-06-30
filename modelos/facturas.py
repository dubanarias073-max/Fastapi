from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import cliente
from datetime import datetime

#El decorador @property proviene de python  y sirve para convertir un metodo  de una clase  en una propiedad de solo lectura
#validacion pydantic v2 , @computed_field es un decorador que te permite definir propiedades o metodos que se calculan dinamicamente
#getattr() es una funcion nativa  de python. sirve para obtener el valor de un atributo o propiedad de un objeto de forma dinamica.

#crear el modelo transacciones (id, fecha, vr_total, cliente)
class FacturaBase(BaseModel):
    fecha:str =datetime.now()
    cliente: cliente # esta es la relacion  con el cliente (objeto)
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
            #calcular(cantidad * vr_unitario)
            return 222

    


class FacturaCrear(FacturaBase):
    pass

class Facturaeditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id :int | None = None