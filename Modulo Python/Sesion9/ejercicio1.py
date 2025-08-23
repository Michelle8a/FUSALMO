'''
Crear un diccionadio donde podamos agregar datos de personas
Nombre, Fecha de Nacimiento

-Identificar la edad a travez de la fecha de nacimiento
-Mencionar el dia de la semana que nacieron

Ej:
Manuel de 35 años de edad y nacio un viernes el 6 de Julio de 1990
'''
from datetime import datetime
import os
import locale

locale.setlocale(locale.LC_TIME, "es_SV.UTF-8")

personas = {}

def agregar_persona(nombre, fecha_nacimiento):

    #paso el string a formato datetime
    formato_fecha = "%d/%m/%Y"
    fecha= datetime.strptime(fecha_nacimiento, formato_fecha) 
    
    hoy = datetime.now() #agarro la fecha de hoy
    edad = hoy.year - fecha.year

    if (hoy.month, hoy.day) < (fecha.month, fecha.day):
        edad -= 1

    dia_semana = fecha.strftime("%A")

    personas[nombre] = {"Nombre" : nombre,
                        "Fecha": fecha_nacimiento,
                        "Edad" : edad,
                        "Dia_Semana": dia_semana}


agregar_persona("Karina", "16/03/1999")

def buscar_personas():
     
     for nombre, datos in personas.items():
            print(f"{nombre} de {datos['Edad']} años y nacio un {datos['Dia_Semana']} el {datos['Fecha']}")


while True:

    os.system('cls')

    print("---AGENDA---")
    print("1. Agregar Nombre")
    print("2. Mostrar Personas")
    print("3. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:

        nombre = input("Ingrese el nombre: ")
        fecha = input("Escribe la fecha de nacimiento en formato dd/mm/aaaa: ")
        agregar_persona(nombre, fecha)


    elif opcion == 2:
        buscar_personas()

    elif opcion == 3:

        print("Saliendo")

    else:

        print("Ingrese una opcion valida")

    input()


