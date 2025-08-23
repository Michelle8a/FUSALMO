'''
Escribir un programa que solicite numeros al usuario 
y muestre la suma y el promedio

'''

numeros = []
print("Introduce numeros uno por uno. Escribe 'x' para terminar")

while True:

    entrada = input("Introduce un numero: ")

    if entrada.lower() == "x":
        break
    try:
        numero = float(entrada)
        numeros.append(numero)

    except ValueError:
        print("Entrada invalida. Introduce un numero o 'x' para salir")

if numeros:

    suma = sum(numeros)
    promedio = suma / len(numeros)
    print(f"\nHas introducido {len(numeros)} numeros.")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.1f}")

else:
    print("No se ingresaron numeros")
