import json
import os

diccionario = {}

while True:
    os.system('cls')
    print("--- MENU ---")
    print("1. Agregar palabra")
    print("2. Descargar archivo")
    print("2. Ver JSON")
    print("4. Salir")

    opcion = int(input("\nElija una opcion: "))

    if opcion == 1:

        key = input("Escriba una palabra: ")
        value = input("Escriba el significado: ")

        diccionario[key] = value
        

    elif opcion == 2:

        file = input("Escriba un nombre para el json: ")

        #nombre del archivo, permiso de edicion, codificacion
        with open (file + ".json", "w", encoding = "utf-8") as archivo:
            json.dump(diccionario, archivo, ensure_ascii=False, indent=4)

        print(f"Archivo descargado como {file}.json")

    elif opcion == 3:

        print("Diccionarios: ")

        for key, value in diccionario.items():
            print(f"{key}: {value}")

    elif opcion == 4:
        print("Saliendo")
        break


    else:
        print("Ingrese una opcion valida")

    input()