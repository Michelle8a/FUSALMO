a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

if a > b:
    print(f"{a} es mayor que {b}")
    print(a, "es mayor que", b)

elif a < b:
    print(f"{a} es menor que {b}")

else:
    print(f"{a} es igual a {b}")