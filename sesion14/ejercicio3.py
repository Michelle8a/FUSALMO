import re

class analizador():
    
    def findall(self, pattern, string):
        return re.findall( pattern, string)


saludo = "Hola mundo, saludos a todos"
a= analizador()
print(a.findall("a", saludo))
print(re.findall("a", saludo))