
x = int(input("Ingrese un numero para mostrar la tabla de multiplicar: "))
i = 1

while i <= 15:
    print(x, "x", i, "=", x * i)

    opcion = input("Desea salir? (s/n)")
    
    if opcion.lower() != 's':
        break

    i += 1
print("Tabla del", x, "generada exitosamente")
