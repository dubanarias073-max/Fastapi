from fastapi import APIRouter, HTTPException, status

from app.modelos.facturas import Factura, FacturaCrear, Facturaeditar
from app.listas import lista_clientes, lista_facturas

rutas_factura = APIRouter()


#endpoint para obtener todas las facturas
@rutas_factura.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


#endpoint para obtener una factura por id
@rutas_factura.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    for obj_factura in lista_facturas:
        if obj_factura.id == factura_id:
            return obj_factura

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}, no existe."
    )


#endpoint para crear una factura
@rutas_factura.post("/facturas", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):

    cliente_encontrado = None

    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe."
        )

    factura_val = Factura.model_validate(datos_factura.model_dump())

    factura_val.id = len(lista_facturas) + 1
    factura_val.cliente = cliente_encontrado

    lista_facturas.append(factura_val)

    return factura_val


#endpoint para editar una factura
@rutas_factura.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Facturaeditar):

    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id_factura:

            datos_actualizados = datos_factura.model_dump(exclude_unset=True)

            factura_val = obj_factura.model_copy(update=datos_actualizados)

            lista_facturas[i] = factura_val

            return factura_val

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {id_factura}, no existe"
    )


#endpoint para eliminar una factura
@rutas_factura.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):

    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id_factura:

            factura_eliminada = lista_facturas.pop(i)

            return factura_eliminada

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {id_factura}, no existe"
    )