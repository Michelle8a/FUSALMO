'''
Crear un programa de python que permita conocer la estructura
geometrica de un triangulo.

Que se puedan definir los lados
Se necesita conocer el area y el perimetro
utilizar funciones

'''
import math

def validarTriangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calcularPerimetro(a, b, c):
    return a + b + c

def calcularArea(a, b, c):
    s = calcularPerimetro(a, b, c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    a = float(input("Ingrese el lado a: "))
    b = float(input("Ingrese el lado b: "))
    c = float(input("Ingrese el lado c: "))

    if not validarTriangulo(a, b, c):
        print("Los lados ingresados no forman un triangulo valido")
        return
    
    perimetro = calcularPerimetro(a, b, c)
    area = calcularArea(a, b, c)
    
    print(f"Perimetro: {perimetro:.2f}")
    print(f"Area: {area:.2f}")


main()