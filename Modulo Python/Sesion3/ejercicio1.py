

suma = 0

while True: #esto genera un ciclo infinitp
    num = int(input("Ingrese un numero (0 para salir): "))
    
    if num == 0:
        break
    
    if num > 0:
        suma += num

print("La suma de los numeros positivos es:", suma)
