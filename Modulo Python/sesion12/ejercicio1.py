'''
Son Hackers eticos y les han pedido extraer información 
documento que no se puede abrir

Abrir con Python el archivo, extraer la información de usuarios 
y contraseñas y luego añadirlos a una lista de diccionario. 

'''
import re
import os

lista = []
lista_limpia = []

os.system("cls")
file = open("sesion12/info.txt", "r", encoding="utf-8")

for line in file: #recorrer el documento linea por linea

    search_user = re.findall("User:", line)
    search_pass = re.findall("Contraseña:", line)

    if len(search_user) > 0:
        user = line.split("User:")
        lista.append(user[1])

    if len(search_pass) > 0:
        password = line.split("Contraseña:")
        lista.append(password[1])        
    

bandera = "user"
diccionario = {
    'User': "",
    'Pass': ""
}

for dato in lista:
    
    dato = dato.strip()
    dato = re.sub("\n", "", dato)

    if bandera == "user":
        diccionario['User'] = dato
        bandera = "pass"

    elif bandera == "pass":
        diccionario['Pass'] = dato
        bandera = "user"

    if diccionario['User'] != "" and diccionario['Pass'] != "":
        print(diccionario)
        lista_limpia.append({
            "User:" : diccionario['User'],
            "Pass:" : diccionario['Pass']
        })

        diccionario['User'] = ""
        diccionario['Pass'] = ""

print(lista_limpia)