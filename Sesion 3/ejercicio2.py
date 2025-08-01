'''
Numeros pares dentro de unrango eprsonalizado

Pide al usuario que ingrese dos numeros: un inicio y un fin
Luego usar range() para mostrar todos los numeros pares dentro de ese rango
(inclusive el inicio y fin si aplican)

'''


inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))

for numero in range(inicio, fin + 1):
    
    if numero % 2 == 0:
        print(numero)
    