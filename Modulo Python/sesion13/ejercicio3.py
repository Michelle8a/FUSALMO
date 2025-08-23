import os

comandos = []

while True:

    print("Menu")
    print("1. Agregar comando")
    print("2. Ver comandos")
    print("3. Ejecutar comando")


    opcion = 0
    
    while True:
        try:
            opcion = int(input("Ingrese su opcion: "))
            break

        except ValueError:
            print("La opcion tiene que ser un numero entero\n")

    if opcion == 1:
        comando = print("Escriba un comando: ")
        comandos.append(comando)


    elif opcion == 2:
        for comando in comandos:
            print(comando)
    

    elif opcion == 3:
        for comando in comandos:
            print(comando)


    elif opcion == 4:
        print("Saliendo")
        break

    else:
        ("Opcion invalida")
    
    input("Presiona Enter para continuar")

    