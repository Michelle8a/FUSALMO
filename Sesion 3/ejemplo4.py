
nombre = input("Ingrese su nombre: ")

for letra in nombre:
    print("Letra:", letra)

#------------------
#recorrer numeros del 1 al 10 con for

for numero in range(1, 11):
    print("Numero:", numero)


#------------------

total_tablas = int(input("Ingrese el numero de tablas de multiplicar que desea generar: "))

for numero in range(1, total_tablas + 1):
    print("Tabla del numero:", numero)

    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x x{multiplicador} = {resultado}")