from fastapi import FastAPI, HTTPException 
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
        status_code=404, detail=f"El cliente con id {cliente_id}, no existe" 
    ) 

#|||||||||||||||||||||||||||| 
#crear los endpoint para facturas 
@app.get("/facturas", response_model=list[Factura]) 
async def listar_facturas(): 
    return lista_facturas 

@app.get("/facturas/{id_factura}", response_model=Factura) 
async def listar_factura(id_factura: int): 
    pass 


@app.post("/facturas", response_model= Factura) 
async def crear_factura(id_cliente:int, datos_factura: FacturaCrear): 
    pass 


@app.patch("/facturas/{id_factura}", response_model= Factura) 
async def editar_factura(id_cliente: int, datos_factura: Facturaeditar): 
    pass 


@app.delete("/facturas/{id_factura}", response_model= Factura) 
async def eliminar_factura(id_factura: int): 
    pass 

#||||||||||||||||||||||||||||||||| 
#crear los endpoint para transacciones 
@app.get("/transacciones", response_model=list[Transaccion]) 
async def listar_transacciones(): 
    pass 

@app.get("/transacciones/{id_transaccion}", response_model=Transaccion) 
async def listar_transaccion(id_transaccion: int): 
    pass 


@app.post("/transacciones", response_model=Transaccion) 
async def crear_transaccion(datos_transaccion: TransaccionCrear): 
    pass 


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion) 
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccioneditar): 
    pass 

@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion) 
async def eliminar_transaccion(id_transaccion: int): 
    pass
