from fastapi import FastAPI
from modelos.clientes import cliente, clientecrear

app = FastAPI()

lista_clientes:list[cliente] = []



#endpoint para obtener todos los clientes 
@app.get("/clientes", response_model=list[cliente])
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
def crear_cliente(datos_cliente: clientecrear):
    cliente_val = cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val

