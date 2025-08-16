
palabra = "arenera"

longitud = len(palabra)

for i in range(0, longitud):

    indice_final = longitud - 1

    i_inverso = indice_final - i
    
    derecho = palabra[i]
    reversa =  palabra[i_inverso]

    print(derecho, "---", reversa)


