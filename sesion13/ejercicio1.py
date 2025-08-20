'''
Crear un archivo que genere una bitacora de incidentes
tiene que tener fecha, incidente y nombre de responsable de registro
'''
import datetime as dt
import os

file_path = "sesion13/bitacora.txt"


while True:

    os.system('cls')
    print("Menu")
    print("1. Agregar Bitacora")
    print("2. Leer Bitacora")
    print("3. Eliminar el archivo")
    print("4. Salir")

    opcion = 0
    
    while True:
        try:
            opcion = int(input("Ingrese su opcion: "))
            break

        except ValueError:
            print("La opcion tiene que ser un numero entero\n")

    if opcion == 1:
        file = open(file_path, "a", encoding=("utf-8"))

        fecha = "\nFecha de Registro: "+ str(dt.datetime.now()) + "\n"
        fecha_inci = input("Escriba la fecha del incidente (dd/mm/aaaa): ")
        #fecha_inci = dt.datetime.strptime(fecha_inci, "%d/%m/%Y")
        #fecha_inci = dt.datetime.strftime("%d/%m/%Y")
        inci = input("Escriba su incidente: ")
        nombre = input("Escriba el nombre del responsable: ")

        file.write(fecha)
        file.write("Incidente: " + inci + "\n")
        file.write("Fecha de Incidente: "+ fecha_inci +"\n")
        file.write("Encargado: "+ nombre + "\n")

        file.close()

    elif opcion == 2:

        file = open(file_path, "r", encoding=("utf-8"))
        print(file.read())
        file.close()

    elif opcion == 2:

        os.remove("sesion13/bitacora.txt")

    elif opcion == 4:
        print("Saliendo")
        break

    else:
        print("Elija una opcion correcta")
    
    input("\nPresione Enter para continuar")

