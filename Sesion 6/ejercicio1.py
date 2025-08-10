'''
Crear una funcion llamada Operar que opere dos variables, 
en los parametros de la funcion sera la opcion de la operacion 
(Suma, resta, multiplicacion, division), despues pasamos de a y b

Solicitar al inicio los valores para a y b

'''
import os

def Operar(opcion, a, b):

    if opcion == 1:
        print(f"Suma: {a + b:.2f}")
    
    elif opcion == 2:
        print(f"Resta: {a - b:.2f}")
    
    elif opcion == 3:
        print(f"Multiplicacion: {a * b:.2f}")
    
    elif opcion == 4:
        
        if b == 0:
            print("No se puede dividir entre 0")
        else:
            print(f"Division: {a / b:.2f}")
    else:
        print("Opcion no valida")


while True:
    os.system('cls')
    print("---MENU---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    op = int(input("Ingrese su opcion: "))

    if op == 5:
        print("Saliendo")
        break

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    Operar(op, num1, num2) 

    input()

   