#Le mete una tupla
def numeros(*tupla):
    
    i= 0
    for numeros in tupla:
        print(f"Posicion {i} = {tupla}")
        i += 1

numeros(2, 5, 6, 4, 1, 9)
    
    