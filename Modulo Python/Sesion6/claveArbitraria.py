'''
** le mete un diccionario a la funcion

Diccionario = {palabra: definicion}
'''

def info(**diccionario):

    for palabra, definicion in diccionario.items():
        print(f"{palabra} = {definicion}")

info(Nombre = "Karina", 
     Edad = 26, 
     Sexo = "Hombre",
     JuegoFavorito = "Slime Rancher")