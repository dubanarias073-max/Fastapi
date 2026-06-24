from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes:list[cliente] = []

#crear modelos cliente (id, nombre , email, descripcion)
class cliente (BaseModel):
    id: int
    nombre:str
    email:str
    descripcion: str

#endpoint para obtener todos los clientes 
@app.get("/clientes")
def listar_clientes():
    return lista_clientes

#endpoint para listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}")
def listar_cliente_por_id(cliente_id: int):
    #recorrer la lista de clientes
    for i,  obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente
    return {"error": "Cliente no encontrado"}

#endpoint para crear un cliente y agregar a la lista
@app.post("/clientes")
def crear_cliente(datos_cliente: cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente

