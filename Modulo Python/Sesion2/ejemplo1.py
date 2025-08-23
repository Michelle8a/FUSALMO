a = int(input("Ingrese un numero: "))

if a % 2 == 0:
    print("El numero es par")

    if a % 3 == 0:
        print("El numero es divisible entre 3")
    
    if a % 5 == 0:
        print("El numero es divisible entre 5")

else:
    print("El numero es impar")