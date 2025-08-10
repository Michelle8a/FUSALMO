#Parametro es la variable que aparece entre parentesis en la definicion de al funcion
#Un argumentos es el valor que se pasa a la funcion

def my_function(name):
    print("Hola", name)

my_function("Manuel")

#----

a = 2
b = 5
c = 10

def suma():
    print(f"La suma de a y b es {a+b+c}")


a = int(input("Actualice el valor de a: "))
b = int(input("Actualice el valor de b: "))
c = int(input("Actualice el valor de c: "))

suma()