import os

ruta = ""

def nombre_archivo():
    nombre = input("Escriba el nombre del archivo: ")
    return nombre

while True:

    try:
        os.system('cls')
        print("Ubicacion actual" + os.getcwd()+"\n")

        print("----MENU----")
        print("1. Ver direcctorios")
        print("2. Mover a directorio")
        print("3. Crear carpeta")
        print("4. Eliminar carpeta")
        print("5. Crear archivo txt")
        print("6. Leer archivo txt")
        print("7. Eliminar archivo txt")
        print("8. Salir")

        opcion = 0

        while True:
            try:
                opcion = int(input("Ingrese su opcion: "))
                break

            except ValueError:
                print("La opcion tiene que ser un numero entero\n")

        if opcion == 1:
            print(os.system("dir")) #Ver carpetas actuales

        elif opcion == 2:
            os.chdir(nombre_archivo()) #Ingresar en la carpeta

        elif opcion == 3:
            os.mkdir(nombre_archivo()) #Crear carpetas

        elif opcion == 4:
            os.rmdir(nombre_archivo()) #Eliminar carpetas

        elif opcion == 5:
            file = open(ruta, "x", encoding=("utf-8"))
            file.close()

        elif opcion == 6:
            archivo = nombre_archivo()
            ruta_archivo = os.path.join(os.getcwd(), archivo)

            if os.path.exists(ruta_archivo):
                rw = print()
            file = open(ruta, "r", encoding=("utf-8"))
            print(file.read())
            file.close()

        elif opcion == 7:
            os.remove(nombre_archivo())

        elif opcion == 8:
            print("Saliendo")
            break

        else:
            ("Opcion invalida")

    except FileExistsError:
        print("El archivo o carpeta existe")

    except FileNotFoundError:
        print("El archivo o carpeta no existe")
    
    
    
    input("Presiona Enter para continuar")
