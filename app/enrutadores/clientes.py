from fastapi import APIRouter, HTTPException, status

from app.modelos.clientes import cliente, clientecrear, clienteeditar
from app.listas import lista_clientes
from app.conexion_bd import Sesion_dependencia
from sqlmodel import select
rutas_clientes = APIRouter()


#endpoint para obtener todos los clientes
@rutas_clientes.get("/clientes", response_model=list[cliente])
async def listar_clientes(sesion: Sesion_dependencia):
    lista_cli =sesion.exec(select(cliente)).all()
    return lista_cli


#endpoint para listar un solo cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=cliente)
async def listar_cliente_por_id(cliente_id: int, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )

    return cliente_bd

#endpoint para crear un cliente y agregar a la lista
@rutas_clientes.post("/clientes", response_model=cliente)
async def crear_cliente(datos_cliente: clientecrear, mi_sesion: Sesion_dependencia):
    cliente_val = cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return cliente_val


#endpoint para editar un cliente y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteeditar, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )
    cliente_dict = datos_cliente.model_dump(exclude_unset=True)
    cliente_bd.sqlmodel_update(cliente_dict)
    mi_sesion.add(cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_bd)
    return cliente_bd
    

#endpoint eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):

    cliente_bd = mi_sesion.get(cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )

    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()

    return cliente_bd