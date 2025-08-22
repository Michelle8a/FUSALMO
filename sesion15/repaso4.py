'''
Escribir un programa que permita almacenar informacion en un archivo

'''


import os

archivo_estudiantes = "estudiantes.txt"

while True:

    os.system('cls')
    print("Menu")
    print("1. Agregar estudiantes")
    print("2. Ver estudiantes")
    print("3. Salir")

    opcion = 0
    
    while True:
        try:
            opcion = int(input("Ingrese su opcion: "))
            break

        except ValueError:
            print("La opcion tiene que ser un numero entero\n")

    if opcion == 1:
        print("Datos del estudiante")

        nombre = input("Ingrese el nombre: ").title() #nombre

        while True: #edad
            try:
                edad = int(input("Ingrese la edad: "))
                break
            except ValueError:
                print("Error: La edad debe ser un numero entero")


        while True: #nota
            try:
                nota = float(input("Ingrese la nota media: "))

                if nota < 0 or nota > 10:
                    print("Error: La nota debe estar entre 0 y 10")
                    continue
                break

            except ValueError:
                print("Error: La nota debe ser un numero valido")

        while True: #sexo
            sexo = input("Ingrese el sexo (M/H): ").upper()
            if sexo == "M":
                sexo = "Mujer"
                break
            elif sexo == "H":
                sexo = "Hombre"
                break
            else:
                print("Error: Ingrese M para Mujer o H para Hombre")

        file = open(archivo_estudiantes, "a", encoding="utf-8")
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Sexo: {sexo}\n")
        file.write(f"Nota Media: {nota}\n")
        file.write("\n")
        file.close()


        print("Estudiante agregado")

    elif opcion == 2:

        if not os.path.exists(archivo_estudiantes) or os.path.getsize(archivo_estudiantes) == 0:
            print("No hay estudiantes registrados")
        else:
            file = open(archivo_estudiantes, "r", encoding="utf-8")
            lineas = file.readlines()
            file.close()

            print("\nLista de estudiantes\n")

            contador = 1
            bloque = []

            for linea in lineas:
                if linea.strip() == "":

                    print(f"Estudiante {contador}:")
                    for dato in bloque:
                        print(dato.strip())
                    print()
                    bloque = []
                    contador += 1
                else:
                    bloque.append(linea)

            if bloque:
                print(f"Estudiante {contador}:")
                for dato in bloque:
                    print(dato.strip())
                print()


    elif opcion == 3:
        print("\nSaliendo")
        break

    else:
        ("Opcion invalida")
    
    input("\nPresiona Enter para continuar")