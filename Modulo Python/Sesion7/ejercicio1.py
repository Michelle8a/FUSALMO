import librerias.areas as areas
import os

while True:
    os.system('cls')

    print("---Menu---")
    print("1. Area de un cuadrado")
    print("2. Area de un rectangulo")
    print("3. Area de un triangulo")
    print("4. Area de un circulo")
    print("5. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado"))
        print("El area es:", areas.area_cuadrado(lado))
    
    elif opcion == 2:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        print("El area es:", areas.area_rectangulo(base, altura))

    elif opcion == 3:
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        print("El area es:", areas.area_triangulo(base, altura))

    elif opcion == 4:
        radio = float(input("Ingrese el radio del circulo: "))
        print("El area es:", areas.area_circulo(radio))
    
    elif opcion == 5:
        print("Saliendo")
        break

    else:
        print("Opcion invalida. Intente de nuevo")

    input()