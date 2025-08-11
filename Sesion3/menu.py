import os
#Menu de acciones para el usuario
while True:
 
    os.system('cls')
    print("Seleccione una acción:")
    print("-----------------------")
 
    print("1. Generar tabla de multiplicar")
    print("2. Repetir acción")
    print("3. Salir")
 
    opcion = input("Seleccione una opción: ")
 
    if opcion == '1':
        x = int(input("Ingrese un número para generar su tabla de multiplicar: "))
        i = 1
        while i <= 10:
            print(x, "x", i, " = ", x * i)
            i += 1
 
    elif opcion == '2':
        print("Repetir accion seleccionada.")
 
    elif opcion == '3':
        print("Saliendo del programa.")
        break  
 
    else:
        print("Opcion no valida, por favor intente de nuevo.")
 
    
    input("\nPresione Enter para continuar...")