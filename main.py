from fastapi import FastAPI

app = FastAPI()

#endpoint
@app.get("/")
def inicio():
    return {"message": "Estoy aprendiendo FastAPI"}
