
def numeros():

    while True:
        try:
            num1 = int(input("\nIngrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            return num1, num2
        
        except ValueError:
            print("Entrada invalida. Los numeros tienen que ser enteros")


def suma():

    a, b = numeros()
    return f"{a} + {b} = {a + b}"


def resta():

    a, b = numeros()
    return f"{a} - {b} = {a - b}"


def multiplicacion():

    a, b = numeros()
    return f"{a} x {b} = {a * b}"


def division():

    while True:
        try:
            a, b = numeros()
            return f"{a} / {b} = {a / b:.2f}"
            
        except ZeroDivisionError:
            print("No se puede dividir entre 0")

    

    