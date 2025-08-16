
palabra = "arenera"

longitud = len(palabra)

for i in range(0, longitud):

    i_inverso = longitud - 1 - i
    
    derecho = palabra[i]
    reversa =  palabra[i_inverso]

    print(derecho, "---", reversa)


