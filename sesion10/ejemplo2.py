'''
Verificar contraseña

Crear una lista qie permita gestionar contraseñas
Añadir contraseñas y validarlas

La contraseñas tiene que tener la siguiente estructura
###:LLL:###
las letras (L) deben ser minusculas
probar contraseñas

1.Agregar contraseñas
2.Ver contraseñas
3.Probar contraseñas (ingresa la contraseña y decir si existe o no)

'''
import os
import re

lista_contra = []
patron = re.compile(r'^\d{3}:[a-z]{3}:\d{3}$')

#Funciones
def checar(contra):
    
    if validar(contra):
        if contra in lista_contra:
            print("La contraseña existe en la lista")
        else:
            print("La contraseña no existe en la lista")
    else:
        print("Contraseña invalida. Debe tener el formato ###:lll:###")


def validar(contra):

    if patron.fullmatch(contra):
        return True
    else:
        return False


def agregar(contra):

    if validar(contra):
        lista_contra.append(contra)
        print("Contraseña agregada")
    else:
        print("Contraseña invalida. Debe tener el formato ###:lll:###")


def ver():

    if lista_contra:
        print("Contraseñas almacenadas:")
        for c in lista_contra:
            print("-", c)
    else:
        print("No hay contraseñas almacenadas")


#Menu
while True:

    os.system('cls')
    print("---MENU---")
    print("1.Agregar contraseñas")
    print("2.Ver contraseñas")
    print("3.Probar contraseñas")
    print("4. Salir")

    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        contraseña = input("Escriba su contraseña (###:lll:###): ")
        agregar(contraseña)

    elif opcion == 2:
        ver()

    elif opcion == 3:
        prueba = input("Ingrese la contraseña para probar: ")
        checar(prueba)

    elif opcion == 4:
        print("Saliendo")
        break

    else:
        print("Elija una opcion valida")

    input()

