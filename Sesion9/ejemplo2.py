import json
import os

#ruta del archivo JSON
ruta = "Sesion9/itca.json"

#abrir y cargar el contenido
with open(ruta, "r", encoding="UTF-8") as archivos:
    datos = json.load(archivos)

for key, value in datos.items():
    print(key, "=", )


i = 0
for productos in datos['cuerpoDocumento']:
    i+= 1
    print("")
    print("Producto", i)
    for key, value in productos.items():
        print(f"{key}: {value}")