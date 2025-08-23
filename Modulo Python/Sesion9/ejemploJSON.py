import json

x = '{"nombre" : "karina", "edad": 26, "ciudad": "ilopango"}'
print(x)
print(type(x))


y = json.loads(x) #convierte el json en diccionario

print(y)
print(type(y))


#--------------

diccionario = {"nombre" : "karina", "edad": 26, "ciudad": "ilopango"}

info = json.dumps(diccionario)
print(info)
print(type(info))
