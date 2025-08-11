a = int(input("Ingrese el limite a: "))
b = int(input("Ingrese el limite b: "))
c = int(input("Ingrese el valor de c: "))


if a <= c and c <= b:
    print("El valor de c esta dentro del rango [a, b]")

else:
    print("El valor de c no esta dentro del rango [a, b]")

    if c < a:
        print("El valor de c es menor que a")
    elif c > b:
        print("El valor de c es mayor que b")