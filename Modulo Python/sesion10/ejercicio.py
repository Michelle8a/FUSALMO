'''
Crear un programa que permita escribir un texto
-que permita contar las palabras especificas
-que permita sustituir palabras
-ver las palabras


'''
import os
import lorem
import re

parrafo = ""

while True:
    os.system('cls')
    print("--- MENU ---")
    print("1. Definir parrafo")
    print("2. Contar todas las palabras")
    print("3. Contar palabras o letras espeficicas")
    print("4. Ver palabras")
    print("5. Sustituir palabras o letras")
    print("6. Salir")

    opcion = int(input("\nElija una opcion: "))

    if opcion == 1:

        generar = input("Desea generar un parrafo con lorem? (y/n): ")

        if generar == "y":
            parrafo = lorem.paragraph()
        
        elif generar == "n":
            parrafo = input("Escriba su parrafo: ")

        else:
            print("Opcion no valida")

    elif opcion == 2:

        palabras = parrafo.split(" ")
        print(f"Total de palabras: {len(palabras)}")

    elif opcion == 3:

        palabra = input("Escriba la palabra a contar: ").lower()
        ocurrencias = re.findall(rf"\b{palabra}\b", parrafo.lower())
        print(f"Total de ocurrencias: {len(ocurrencias)}")


    elif opcion == 4:
        
        print(parrafo)
        palabras = parrafo.split(" ") #Devuelve una lista
        print(palabras)
        print(f"Total de palabras: {len(palabras)}")

    elif opcion == 5:
        palabra_buscar = input("Escriba la palabra que desea buscar: ").lower()
        palabra_reemplazar = input("Escriba la palabra para reemplazar: ")

        tokens = re.findall(r'\w+|\W+', parrafo)
        for i in range(len(tokens)):
            if tokens[i].isalpha() and tokens[i].lower() == palabra_buscar:
                tokens[i] = palabra_reemplazar
                parrafo = ''.join(tokens)


    elif opcion == 6:
        print("Saliendo")
        break


    else:
        print("Ingrese una opcion valida")

    input()



