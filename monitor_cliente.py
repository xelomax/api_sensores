import requests

# URL del endpoint de la API que entrega el listado de sensores
url = "http://127.0.0.1:8000/sensores"

# Encabezado con la clave API necesaria para acceder al endpoint
headers = {
    "x-api-key": "marcelo_ulloa"
}

# Se realiza una solicitud GET a la API
respuesta = requests.get(url, headers=headers)

# Se valida si la respuesta de la API fue correcta
if respuesta.status_code == 200:
    # Se convierte la respuesta JSON en datos que Python pueda utilizar
    datos = respuesta.json()

    print("Monitoreo de sensores industriales")
    print("----------------------------------")

    # Se recorren los sensores recibidos desde la API
    for sensor in datos["sensores"]:
        print("ID:", sensor["id"])
        print("Nombre:", sensor["nombre"])
        print("Ubicación:", sensor["ubicacion"])
        print("Valor:", sensor["valor"], sensor["unidad"])
        print("----------------------------------")

else:
    # Si ocurre un error, se muestra el código y el detalle entregado por la API
    print("Error al consultar la API")
    print("Código de estado:", respuesta.status_code)
    print("Detalle:", respuesta.text)