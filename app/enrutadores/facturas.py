from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.modelos.clientes import cliente
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer
from app.conexion_bd import Sesion_dependencia

rutas_factura = APIRouter()


#endpoint para obtener todas las facturas
@rutas_factura.get("/facturas", response_model=list[FacturaLeer])
async def listar_facturas(sesion: Sesion_dependencia):
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


#endpoint para obtener una factura por id
@rutas_factura.get("/facturas/{factura_id}", response_model=FacturaLeer)
async def obtener_factura(factura_id: int, sesion: Sesion_dependencia):

    factura_bd = sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id}, no existe."
        )

    return factura_bd


#endpoint para crear una factura
@rutas_factura.post("/facturas", response_model=FacturaLeer)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion: Sesion_dependencia):

    #buscar el cliente en la base de datos
    cliente_encontrado = sesion.get(cliente, cliente_id)

    #mensaje si el cliente no fue encontrado
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con id {cliente_id}, no existe."
        )

    #validar datos de la factura
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id

    factura_val = Factura.model_validate(factura_dict)

    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)

    return factura_val


#endpoint para editar una factura
@rutas_factura.patch("/facturas/{factura_id}", response_model=FacturaLeer)
async def editar_factura(
    factura_id: int,
    datos_factura: FacturaEditar,
    sesion: Sesion_dependencia
):

    factura_bd = sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id}, no existe."
        )

    datos_actualizados = datos_factura.model_dump(exclude_unset=True)

    factura_bd.sqlmodel_update(datos_actualizados)

    sesion.add(factura_bd)
    sesion.commit()
    sesion.refresh(factura_bd)

    return factura_bd


#endpoint para eliminar una factura
@rutas_factura.delete("/facturas/{factura_id}", response_model=FacturaLeer)
async def eliminar_factura(
    factura_id: int,
    sesion: Sesion_dependencia
):

    factura_bd = sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id}, no existe."
        )

    sesion.delete(factura_bd)
    sesion.commit()

    return factura_bd