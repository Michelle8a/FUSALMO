'''
Ejercicio: Gestion de estudiantes y calificaciones
supon que tienes una lista de diccionarios, 
donde cada diccionario representa a un estudiante con su nombre,
edad y una lista de calificaciones.

Tareas: 
-Calcular el promedio de calificaciones por estudiante y agregarlo al diccionario
con la clave "promedio"
-Mostrar el nombre del estudiante con el promedio mas alto
-Ordenar la lista de estudiantes por promedio de mayor a menor

'''

# lista(diccionario(calificaciones))

estudiantes = [
    {"Nombre": "Karina",
     "Edad": 26,
     "Calificaciones": [10, 20, 30, 40, 50],
     "Promedio": 0
    },
    {"Nombre": "Luis",
     "Edad": 12,
     "Calificaciones": [40, 50, 60],
     "Promedio": 0
    },
    {"Nombre": "Mauricio",
     "Edad": 19,
     "Calificaciones": [70, 80, 90, 100],
     "Promedio": 0
    }
]

for estudiante in estudiantes: #para ver cada estudiante
    suma = 0
    for calificacion in estudiante["Calificaciones"]: #para ver las notas de cada uno
        suma += calificacion

    promedio = suma / len(estudiante["Calificaciones"])
    estudiante["Promedio"] = promedio #meto el promedio que calcule en el diccionario


print("Promedios de los estudiantes:")
for estudiante in estudiantes:
    print(f"{estudiante['Nombre']} (Edad: {estudiante['Edad']}): Promedio = {estudiante['Promedio']}")
