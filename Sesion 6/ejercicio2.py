
def esPrimo (numero):

    for x in range(2, numero):
        if numero % x == 0:
            return False

    return True


num1 = int(input("Ingrse un numero para saber si es primo: "))

if esPrimo(num1):
    print(f"El numero {num1} es primo")

else:
    print("El numero no es primo")