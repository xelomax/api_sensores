# API de monitoreo de sensores industriales

Trabajo local desarrollado con FastAPI para consultar, registrar y eliminar sensores industriales simulados.

## Requisitos

- Python 3
- FastAPI
- Uvicorn
- Requests

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la API

```bash
uvicorn main:app --reload
```

La API queda disponible en:

```text
http://127.0.0.1:8000
```

La documentacion interactiva de FastAPI queda en:

```text
http://127.0.0.1:8000/docs
```

## Clave API

Para usar los endpoints se debe enviar el encabezado:

```text
x-api-key: marcelo_ulloa
```

## Endpoints

- `GET /sensores`: lista los sensores registrados.
- `POST /sensores`: registra un nuevo sensor.
- `DELETE /sensores/{sensor_id}`: elimina un sensor por ID.

## Cliente de monitoreo

Con la API ejecutandose, se puede probar el cliente con:

```bash
python monitor_cliente.py
```
