import agenda
import os

while True:

    os.system('cls')

    print("---AGENDA---")
    print("1. Agregar Contacto")
    print("2. Buscar Contacto")
    print("3. Mostar Contactos")
    print("4. Eliminar Contacto")
    print("5. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:

        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")

        agenda.agregar_contacto(nombre, telefono)

    elif opcion == 2:

        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)

    elif opcion == 3:
        
        print("\n---CONTACTOS---")
        agenda.mostrar_agenda()

    elif opcion == 4:

        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        agenda.eliminar_contacto(nombre)
    
    elif opcion == 5:

        print("Saliendo")
        break

    else:
        print("Ingrese una opcion valida")

    input("Presione Enter para continuar")




