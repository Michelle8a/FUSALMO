
i = 1

while True:
    print("Repeticion", i)

    opcion = input("Desea salir? (s/n)")
    
    if opcion.lower() != 'n':
        break
    
    elif opcion.lower() == 's':
        i += 1

    else:
        print("Opcion no valida")

print("Se repitio i veces: ", i)