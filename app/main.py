from fastapi import FastAPI
from enrutadores import clientes
from enrutadores import facturas
from enrutadores import transacciones

app = FastAPI()

# Incluir rutas
app.include_router(clientes.rutas_clientes, tags=["Clientes"])
app.include_router(facturas.rutas_factura, tags=["Facturas"])
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])