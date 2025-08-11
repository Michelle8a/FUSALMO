x = int(input("Ingrese un numero para mostrar la tabla de multiplicar: "))
i = 0

while i <= 10:
    
    i = i + 1

    if i % 2 == 0:
        continue
    
    print(x, "x", i, "=", x * i)
    

print("Tabla del", x, "generada exitosamente")
