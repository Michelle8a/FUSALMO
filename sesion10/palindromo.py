
palabra = "arenera"

longitud = len(palabra)

for i in range(0, longitud):

    indice_final = longitud - 1

    i_inverso = indice_final - i
    
    derecho = palabra[i]
    reversa =  palabra[i_inverso]

    print(derecho, "---", reversa)


#------

palabra = input("Escriba una palabra: ")
es_palindromo = True 

for i in range(len(palabra)):
   
    if palabra[i] != palabra[len(palabra) - 1 - i]:
        es_palindromo = False
        break

if es_palindromo:
    print("Si es palindromo")
else:
    print("No es palindromo")