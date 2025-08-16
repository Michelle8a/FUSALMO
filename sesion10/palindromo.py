
palabra = "arenera"

for i in range(0, len(palabra)):

    i_inverso = len(palabra) - 1 - i
    
    derecho = palabra[i]
    reversa =  palabra[i_inverso]

    print(derecho, "---", reversa)


