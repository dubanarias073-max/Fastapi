from fastapi import FastAPI, HTTPException
from modelos.clientes import cliente, clientecrear, clienteeditar

app = FastAPI()

lista_clientes:list[cliente] = []



#endpoint para obtener todos los clientes 
@app.get("/clientes", response_model=list[cliente])
async def listar_clientes():
    return lista_clientes

#endpoint para listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}")
async def listar_cliente_por_id(cliente_id: int):
    #recorrer la lista de clientes
    for i,  obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    return {"error": "Cliente no encontrado"}

#endpoint para crear un cliente y agregar a la lista
@app.post("/clientes")
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = cliente.model_validate(datos_cliente.model_dump())
    #generar el id
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

#endpoint para editar un cliente y agregar a la lista
@app.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente : clienteeditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            datos_actualizados = datos_cliente.model_dump(exclude_unset=True)
            cliente_val = obj_cliente.model_validate(datos_cliente.model_dump())
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(status_code=404, detail=f"El cliente con id {cliente_id}, no existe")
