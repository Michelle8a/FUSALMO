import math

mayor = max(1, 2, 3, 4, 5, 6)
print(mayor)

menor = [1.5, 2.50, 3.0, 4.36, 5.8, 6.5, 1.4]
print(min(menor))

#valor absoluto
print(abs(-7), "-", abs(7))

#potencia
print(f"2^3 = {2**3} ")
print(f"2^3 =", pow(2, 3))


#---Estas si ocupan el modulo

print(f"La raiz cuadrada de 25 es", pow(25, 1/2))
print(f"La raiz cuadrada de 25 es", math.sqrt(25))

print("ceil de 6.5 = ", math.ceil(6.5))
print("floor de 6.5 = ", math.floor(6.5))