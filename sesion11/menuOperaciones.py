'''
Hacer un programa de operaciones basicas
1. Sumar
2. Restar
3. Multiplicar
4. Dividir

'''
import os
import operaciones as op


while True:
    os.system('cls')
    print("---MENU---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = 0

    while True:
        try:
            opcion = int(input("Ingrese su opcion: "))
            break

        except ValueError as e:
            print("La opcion tiene que ser un numero entero\n")
            
            print("Tipo de error:", type(e))
            print("Error:", e)
    
    if opcion == 1:
        print(op.suma())
                
    elif opcion == 2:
        print(op.resta())
                
    elif opcion == 3:
        print(op.multiplicacion())
                
    elif opcion == 4:
        print(op.division())

    elif opcion == 5:
        print("Saliendo")
        break

    else:
        print("Opcion no valida")
    
    input("Presione Enter para continuar")





