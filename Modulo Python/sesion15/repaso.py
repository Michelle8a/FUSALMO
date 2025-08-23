
for letra in "Palabra":
    print(letra)


lista = [1, 2, 3, 4, 5]
print(lista[2])

for numero in lista:
    print(numero)


for i in range(0, 10):
    print(i)


for i in [True, 2, "tres", 4.0, [5], (6), {7: "siete"}, {8}]:
    print(i)

diccionario = {"nombre": "juan", 
               "edad": 30,
               "ciudad": "Madrid"}

for key, item in diccionario.items():
    print(f"{key}: {item}")