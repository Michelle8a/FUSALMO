lista = []

while True:
    fruta = input("Introduce una fruta ('salir para temrinar')")

    if fruta.lower() == "salir":
        break
        
    lista.append(fruta)
    
print("Lista de frutas ingresadas:")

#de cualquiera de las dos maneras
for i, fruta in enumerate(lista, start = 1):
    print(f"{i}. {fruta}")


for i in range(len(lista)):
    print(f"{i + 1}. {lista[i]}")