import os

while True:

    os.system('cls')
    print("Menu")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Salir")

    opcion = 0
    
    while True:
        try:
            opcion = int(input("Ingrese su opcion: "))
            break

        except ValueError:
            print("La opcion tiene que ser un numero entero\n")

    if opcion == 1:
        pass

    elif opcion == 2:
        pass

    elif opcion == 3:
        print("Saliendo")
        break

    else:
        ("Opcion invalida")
    
    input("Presiona Enter para continuar")



