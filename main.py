from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel

# Se crea la aplicación principal de FastAPI
app = FastAPI(
    title="API de monitoreo de sensores industriales",
    description="API REST para consultar, registrar y eliminar datos de sensores en un sistema automatizado",
    version="1.0"
)

# Clave que se usará para proteger la API
API_KEY = "marcelo_ulloa"

# Lista con sensores simulados
# Estos datos representan sensores industriales básicos
sensores = [
    {
        "id": 1,
        "nombre": "Sensor de temperatura",
        "ubicacion": "Sala de máquinas",
        "valor": 32.5,
        "unidad": "°C"
    },
    {
        "id": 2,
        "nombre": "Sensor de presión",
        "ubicacion": "Línea de producción",
        "valor": 7.8,
        "unidad": "bar"
    }
]

# Modelo que define los datos que debe tener un sensor nuevo
class Sensor(BaseModel):
    nombre: str
    ubicacion: str
    valor: float
    unidad: str

# Función que valida si la clave API enviada por el cliente es correcta
def validar_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Clave API no autorizada"
        )
    return x_api_key

# Endpoint GET
# Permite consultar todos los sensores registrados
@app.get("/sensores", dependencies=[Depends(validar_api_key)])
def obtener_sensores():
    return {
        "mensaje": "Listado de sensores registrados",
        "sensores": sensores
    }

# Endpoint POST
# Permite agregar un nuevo sensor a la lista
@app.post("/sensores", dependencies=[Depends(validar_api_key)])
def crear_sensor(sensor: Sensor):
    nuevo_id = len(sensores) + 1

    # Se crea un nuevo sensor con los datos recibidos
    nuevo_sensor = {
        "id": nuevo_id,
        "nombre": sensor.nombre,
        "ubicacion": sensor.ubicacion,
        "valor": sensor.valor,
        "unidad": sensor.unidad
    }

    # Se agrega el nuevo sensor a la lista
    sensores.append(nuevo_sensor)

    return {
        "mensaje": "Sensor registrado correctamente",
        "sensor": nuevo_sensor
    }

# Endpoint DELETE
# Permite eliminar un sensor usando su ID
@app.delete("/sensores/{sensor_id}", dependencies=[Depends(validar_api_key)])
def eliminar_sensor(sensor_id: int):
    for sensor in sensores:
        if sensor["id"] == sensor_id:
            sensores.remove(sensor)
            return {
                "mensaje": "Sensor eliminado correctamente",
                "sensor_eliminado": sensor
            }

    # Si no encuentra el sensor, devuelve un error 404
    raise HTTPException(
        status_code=404,
        detail="Sensor no encontrado"
    )