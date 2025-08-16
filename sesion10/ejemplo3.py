import re

#funcion findall
texto = "123123456123"
x = re.findall("1", texto) #genera una lista
print(x)
print("Cantidad de ocurrencias:", len(x))


#funcion search
texto2 = "Hola mundo"
y = re.search(" ", texto2)
print(y)

