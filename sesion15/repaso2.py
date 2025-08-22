'''
Crear un programa de python que solicite al usuario
un numero para poder mostrar la tabla de multiplicar

Validar que sea un numero entero positivo
'''


try:

    numero = int(input("Ingrese un numero: "))

    if numero < 0:
        raise ValueError("El numero debe ser positivo")

    else:
        print(f"Tabla de multiplicar del {numero}")

        for i in range(1, 11):
            print(f"{numero} x {i} = {numero*i}")

except ValueError as e:
    print(f"Error: {e}")
