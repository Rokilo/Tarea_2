import uvicorn
from fastapi import FastAPI
from api_data import Data

app = FastAPI()
Archivo = open("datos.txt","r")
Datos = Data(Archivo)

@app.get("/")
def index():
    return "¡Bienvenido! Para poder ingresar a su cuenta, agregue un '/login/' a la URL, seguido de su contraseña. Ejemplo: 127.0.0.1:80/login/MiContraseña"

@app.get("/login/{password}")
async def info_getter(password:str):
    Info = Datos.Buscar_Data(password)
    print(Info)
    return Info

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)