from fastapi import APIRouter, HTTPException, status

from app.modelos.facturas import Factura
from app.modelos.transacciones import (
    Transaccion,
    TransaccionCrear,
    Transaccioneditar,
)

from app.listas import lista_transacciones, lista_facturas

rutas_transacciones = APIRouter()


@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones


@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    for obj_transaccion in lista_transacciones:
        if obj_transaccion.id == id_transaccion:
            return obj_transaccion

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"La transaccion con id {id_transaccion}, no existe."
    )


@rutas_transacciones.post("/transacciones", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):

    factura_encontrada = None

    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
            break

    if factura_encontrada is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())

    transaccion_val.id = len(lista_transacciones) + 1
    transaccion_val.factura_id = factura_encontrada.id

    lista_transacciones.append(transaccion_val)
    factura_encontrada.transacciones.append(transaccion_val)

    return transaccion_val


@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccioneditar):

    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:

            datos_actualizados = datos_transaccion.model_dump(exclude_unset=True)

            transaccion_val = obj_transaccion.model_copy(update=datos_actualizados)

            lista_transacciones[i] = transaccion_val

            return transaccion_val

    raise HTTPException(
        status_code=404,
        detail=f"La transaccion con id {id_transaccion}, no existe"
    )


@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):

    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:

            transaccion_eliminada = lista_transacciones.pop(i)

            return transaccion_eliminada

    raise HTTPException(
        status_code=404,
        detail=f"La transaccion con id {id_transaccion}, no existe"
    )