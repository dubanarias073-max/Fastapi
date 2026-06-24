# PROYECTO CLIENTES - FASTAPI

## 👤 Información del Desarrollador

* **Nombre:** Duban Alejandro Arias Bejarano
* **Ficha:** 3407184

---

# 📁 Estructura del Proyecto

```text
FASTAPI/
│
├── models/                           
│   └── cliente.py            
│
├── routers/                  
│   └── clientes.py           
│
├── venv/                     
├── base_datos.db             
├── database.py               
├── main.py                   
├── readme.md                 
└── requirements.txt          
```

---

# 📌 Descripción

Proyecto desarrollado con FastAPI utilizando arquitectura modular, SQLite y SQLAlchemy.

La API permite administrar:

* Clientes
* Facturas
* Transacciones

Incluye operaciones CRUD completas:

* GET
* POST
* PUT
* DELETE

---

# 🛠️ Tecnologías Utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

# 🚀 Instrucciones de Ejecución (Windows)

## 1️⃣ Crear entorno virtual

```bash
python -m venv venv
```

---

## 2️⃣ Activar entorno virtual

```bash
venv\Scripts\activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install "fastapi[standard]" sqlalchemy
```

---

## 4️⃣ Ejecutar servidor

```bash
fastapi dev main.py
```

---

# 🌐 Documentación Swagger

Una vez ejecutado el servidor, ingresar a:

```text
http://127.0.0.1:8000/docs
```

---

# 📌 Funcionalidades

## 👥 Clientes

* Crear clientes
* Consultar clientes
* Actualizar clientes
* Eliminar clientes

## 🧾 Facturas

* Crear facturas
* Consultar facturas
* Actualizar facturas
* Eliminar facturas

## 💳 Transacciones

* Crear transacciones
* Consultar transacciones
* Actualizar transacciones
* Eliminar transacciones

---

# 📄 requirements.txt

```txt
fastapi[standard]
sqlalchemy
pydantic
uvicorn
```

---




# ✅ Autor

**Duban Alejandro Arias Bejarano**
Ficha ADSO: **3407184**