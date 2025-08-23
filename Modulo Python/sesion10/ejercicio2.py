
import json
import os

bd = "productos.json"
datos = {}

if os.path.exists(bd):
    with open(bd, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
else:
    datos = {}

while True:

    os.system('cls')
    print("--- MENU ---")
    print("1. Ver productos")
    print("2. Agregar productos")
    print("3. Eliminar Productos")
    print("4. Modificar Productos")
    print("5. Salir")

    opcion = int(input("\nElija una opcion: "))

    if opcion == 1:

        print("\n---- PRODUCTOS ----")

        for key, value in datos.items():
            print(f"{key}: {value}")


    elif opcion == 2:

        producto = input("Escriba una palabra: ")
        precio = float(input("Escriba el significado: "))

        datos[producto] = precio


    elif opcion == 3:

        producto = input("Escriba el producto a eliminar")
        datos.pop(producto)

    elif opcion == 4:

        producto = input("Escriba el producto a modificar: ")

        nuevo_producto = input("Escriba el nuevo producto: ")
        nuevo_precio = float(input("Escriba el nuevo precio: "))
        
        datos.pop(producto)
        datos[nuevo_producto] = nuevo_precio

    elif opcion == 5:
        print("Saliendo")
        break

    else:
        print("Ingresa una opcion valida")

    input("\nPresiona cualquier tecla para continuar")
    with open (bd, "w", encoding = "utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)