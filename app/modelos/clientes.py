from pydantic import BaseModel

#crear modelos cliente (id, nombre , email, descripcion)
class clienteBase(BaseModel):
    nombre:str
    email:str
    descripcion: str

class clientecrear(clienteBase):
    pass

class clienteeditar(clienteBase):
    pass

class cliente(clienteBase):
    id:int | None = None