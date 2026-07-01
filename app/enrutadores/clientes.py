from fastapi import APIRouter, HTTPException

from modelos.clientes import cliente, clientecrear, clienteeditar
from listas import lista_clientes

rutas_clientes = APIRouter()


#endpoint para obtener todos los clientes
@rutas_clientes.get("/clientes", response_model=list[cliente])
async def listar_clientes():
    return lista_clientes


#endpoint para listar un solo cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=cliente)
async def listar_cliente_por_id(cliente_id: int):
    for obj_cliente in lista_clientes:
        if obj_cliente.id == cliente_id:
            return obj_cliente

    raise HTTPException(
        status_code=400,
        detail=f"El cliente con id {cliente_id}, no existe."
    )


#endpoint para crear un cliente y agregar a la lista
@rutas_clientes.post("/clientes", response_model=cliente)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = cliente.model_validate(datos_cliente.model_dump())

    cliente_val.id = len(lista_clientes) + 1

    lista_clientes.append(cliente_val)

    return cliente_val


#endpoint para editar un cliente y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteeditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:

            datos_actualizados = datos_cliente.model_dump(exclude_unset=True)

            cliente_val = obj_cliente.model_copy(update=datos_actualizados)

            lista_clientes[i] = cliente_val

            return cliente_val

    raise HTTPException(
        status_code=404,
        detail=f"El cliente con id {cliente_id}, no existe"
    )


#endpoint eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:

            cliente_eliminado = lista_clientes.pop(i)

            return cliente_eliminado

    raise HTTPException(
        status_code=400,
        detail=f"El cliente con id {cliente_id}, no existe"
    )