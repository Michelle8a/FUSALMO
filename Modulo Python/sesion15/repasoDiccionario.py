'''
Crear una lista de estudiantes, los valores que necesitamos por estudiante
son el nombre, la edad, el sexo, nota media

un ciclo infinito para ir pidiendo los datos de los estudiantes
y guardarlos en una lista, colocar una opcion para ver los estudiantes
y otra opcion para salir del programa
'''

import os

estudiantes = []

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

        #meto la informacion en forma de diccionario a la lista
        estudiantes.append({"Nombre": nombre,
                            "Edad": edad,
                            "Sexo": sexo,
                            "Nota_Media": nota})
        
        print("Estudiante agregado")

    elif opcion == 2:

        if not estudiantes:
            print("No hay estudiantes registrados")
        
        else:
            print("\nLista de estudiantes\n")

            contador = 1

            for estudiante in estudiantes: #recorre cada item de la lista (cada diccionario)
                print(f"Estudiante {contador}:")

                for key, value in estudiante.items(): #recorre cada informacion del diccionario
                    print(f"{key}: {value}")

                print()
                contador += 1

    elif opcion == 3:
        print("\nSaliendo")
        break

    else:
        ("Opcion invalida")
    
    input("\nPresiona Enter para continuar")


