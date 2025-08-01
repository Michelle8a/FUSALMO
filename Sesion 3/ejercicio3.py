'''
Numeros primos

'''

inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))

print(f"\nNumeros primos entre {inicio} y {fin}:")

for num in range(inicio, fin + 1):
    
    if num < 2:
        continue 

    es_primo = True

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(num)

