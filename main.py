from fastapi import FastAPI, HTTPException, status 
from modelos.clientes import cliente, clientecrear, clienteeditar 
from modelos.facturas import Factura, FacturaCrear, Facturaeditar 
from modelos.transacciones import Transaccion, TransaccionCrear ,Transaccioneditar 

app = FastAPI() 

lista_clientes:list[cliente] = [] 
lista_facturas:list[Factura]=[] 
lista_transacciones:list[Transaccion]=[] 

#endpoint para obtener todos los clientes 
@app.get("/clientes", response_model=list[cliente]) 
async def listar_clientes(): 
    return lista_clientes 

#endpoint para listar un solo cliente de la lista 
@app.get("/clientes/{cliente_id}") 
async def listar_cliente_por_id(cliente_id: int): 
    #recorrer la lista de clientes 
    for i, obj_cliente in enumerate(lista_clientes): 
        if obj_cliente.id == cliente_id: 
            return obj_cliente 
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )

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
            # CORRECCIÓN: Se usa model_copy(update=...) para aplicar los cambios sobre el objeto existente
            cliente_val = obj_cliente.model_copy(update=datos_actualizados) 
            lista_clientes[i] = cliente_val 
            return cliente_val 
    raise HTTPException(status_code=404, detail=f"El cliente con id {cliente_id}, no existe") 

#endpoint eliminar cliente 
@app.delete("/clientes/{cliente_id}", response_model=cliente) 
async def eliminar_cliente(cliente_id:int): 
    for i , obj_cliente in enumerate(lista_clientes): 
        if obj_cliente.id == cliente_id: 
            cliente_eliminado = lista_clientes.pop(i) 
            return cliente_eliminado 
    raise HTTPException( 
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe" 
    ) 

#|||||||||||||||||||||||||||| 
#crear los endpoint para facturas 
@app.get("/facturas", response_model=list[Factura]) 
async def listar_facturas(): 
    return lista_facturas 

@app.get("/facturas/{factura_id}", response_model=Factura) 
async def listar_factura(factura_id: int): 
    #recorrer la lista de facturas
    for i, obj_factura in enumerate(lista_facturas): 
        if obj_factura.id == factura_id: 
            return obj_factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe.")

@app.post("/facturas", response_model=Factura) 
async def crear_factura(id_cliente: int, datos_factura: FacturaCrear): 
    cliente_existe = False
    for obj_cliente in lista_clientes:
        if obj_cliente.id == id_cliente:
            cliente_existe = True
            break
    if not cliente_existe:
        raise HTTPException(status_code=400, detail=f"El cliente con id {id_cliente} no existe.")
        
    factura_val = Factura.model_validate(datos_factura.model_dump()) 
    factura_val.id = len(lista_facturas) + 1
    factura_val.id_cliente = id_cliente
    lista_facturas.append(factura_val)
    return factura_val

@app.patch("/facturas/{id_factura}", response_model=Factura) 
async def editar_factura(id_factura: int, datos_factura: Facturaeditar): 
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id_factura:
            datos_actualizados = datos_factura.model_dump(exclude_unset=True)
            factura_val = obj_factura.model_copy(update=datos_actualizados)
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(status_code=404, detail=f"La factura con id {id_factura}, no existe")

@app.delete("/facturas/{id_factura}", response_model=Factura) 
async def eliminar_factura(id_factura: int): 
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id_factura:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=404, detail=f"La factura con id {id_factura}, no existe")

#||||||||||||||||||||||||||||||||| 
#crear los endpoint para transacciones 
@app.get("/transacciones", response_model=list[Transaccion]) 
async def listar_transacciones(): 
    return lista_transacciones

@app.get("/transacciones/{id_transaccion}", response_model=Transaccion) 
async def listar_transaccion(id_transaccion: int): 
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            return obj_transaccion
    raise HTTPException(status_code=404, detail=f"La transaccion con id {id_transaccion}, no existe")

@app.post("/transacciones", response_model=Transaccion) 
async def crear_transaccion(datos_transaccion: TransaccionCrear): 
    factura_asociada = None
    for obj_factura in lista_facturas:
        if obj_factura.id == datos_transaccion.id_factura:
            factura_asociada = obj_factura
            break
    if not factura_asociada:
        raise HTTPException(status_code=400, detail=f"La factura con id {datos_transaccion.id_factura} no existe.")
        
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.id = len(lista_transacciones) + 1
    transaccion_val.id_cliente = factura_asociada.id_cliente
    lista_transacciones.append(transaccion_val)
    return transaccion_val

@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion) 
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccioneditar): 
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            datos_actualizados = datos_transaccion.model_dump(exclude_unset=True)
            transaccion_val = obj_transaccion.model_copy(update=datos_actualizados)
            lista_transacciones[i] = transaccion_val
            return transaccion_val
    raise HTTPException(status_code=404, detail=f"La transaccion con id {id_transaccion}, no existe")

@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion) 
async def eliminar_transaccion(id_transaccion: int): 
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            transaccion_eliminada = lista_transacciones.pop(i)
            return transaccion_eliminada
    raise HTTPException(status_code=404, detail=f"La transaccion con id {id_transaccion}, no existe")
