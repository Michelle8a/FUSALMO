
try:
    palabra = "manuel"
    print(f"Cantidad de letras: {len(palabra)}") #len = 6: numero de letras
    print(palabra[len(palabra) -1]) #Quitar -1 genera error

    palabra[0] #m
    palabra[1] #a
    palabra[2] #n
    palabra[3] #u
    palabra[4] #e
    palabra[5] #l
    palabra[6] #Ya no existe nada


    diccionario = {
        "Nombre": "Manuel"
    }

    print(diccionario["apellido"]) #apellido no existe en el diccionario

except KeyError:
    print("Key en el diccionario no disponible")

except IndexError:
    print("Letra no disponible")






