# 🚀 API REST - Gestión de Clientes, Facturas y Transacciones

## 👨‍💻 Desarrollador

- **Nombre:** Duban Alejandro Arias Bejarano
- **Programa:** ADSO
- **Ficha:** 3407184

---

# 📖 Descripción

Proyecto desarrollado con **FastAPI** y **SQLModel** para administrar clientes, facturas y transacciones mediante una API REST.

La aplicación implementa una arquitectura modular separando los modelos de la base de datos y los enrutadores para facilitar el mantenimiento y la escalabilidad del proyecto.

---

# 📁 Estructura del Proyecto

```text
FASTAPI/
│
├── app/
│   ├── enrutadores/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── modelos/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── conexion_bd.py
│   └── main.py
│
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🛠 Tecnologías Utilizadas

- Python 3.12+
- FastAPI
- SQLModel
- Pydantic
- Uvicorn

---

# ⚙ Instalación

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

Entrar al proyecto

```bash
cd FASTAPI
```

---

## 2. Crear el entorno virtual

```bash
python -m venv venv
```

---

## 3. Activar el entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶ Ejecutar el servidor

Con FastAPI:

```bash
fastapi dev app/main.py
```

O utilizando Uvicorn:

```bash
uvicorn app.main:app --reload
```

---

# 📚 Documentación

Una vez iniciado el servidor, acceder a:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📌 Funcionalidades

## 👤 Clientes

- Crear clientes
- Consultar todos los clientes
- Consultar cliente por ID
- Actualizar clientes
- Eliminar clientes

---

## 🧾 Facturas

- Crear facturas
- Consultar facturas
- Actualizar facturas
- Eliminar facturas
- Asociación con clientes

---

## 💳 Transacciones

- Crear transacciones
- Consultar transacciones
- Actualizar transacciones
- Eliminar transacciones
- Asociación con facturas
- Cálculo automático del valor total de cada factura

---

# 🗂 Arquitectura

El proyecto está organizado siguiendo una estructura modular:

- **app/modelos/** → Contiene los modelos de SQLModel.
- **app/enrutadores/** → Contiene los endpoints de la API.
- **conexion_bd.py** → Configuración de la conexión a la base de datos.
- **main.py** → Punto de entrada de la aplicación.

---

# 📦 Dependencias

Contenido del archivo **requirements.txt**

```txt
fastapi[standard]
sqlmodel
uvicorn
```

---

# 📄 Licencia

Proyecto desarrollado con fines académicos para el programa **Análisis y Desarrollo de Software (ADSO)** del **SENA**.

---

# ✨ Autor

**Duban Alejandro Arias Bejarano**

**ADSO - Ficha 3407184**