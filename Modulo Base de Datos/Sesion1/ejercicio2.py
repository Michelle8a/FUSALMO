from pymongo import MongoClient
import connection as net

# Conexión al cluster de MongoDB Atlas
db = net.client["mydatabase"]
collection = db["students"]


# Función para crear un estudiante
def create_student():
    student = {}
    while True:
        print("\nAñadir Propiedades:")
        key = input("Ingrese el nombre de la propiedad (o 'salir' para regresar): ")
        if key == "salir":
            break
        value = input("Ingrese el valor de la propiedad: ")
        student[key] = value

    collection.insert_one(student)
    print("Estudiante creado y subido al servidor exitosamente.")

# Función para mostrar estudiantes añadidos a la nube
def show_students():
    students = collection.find()
    for student in students:
        print(student)

# Menú principal
while True:
    print("\n--- Menú Principal ---")
    print("a. Crear Estudiante")
    print("b. Mostrar estudiantes añadidos a la nube")
    print("c. Salir")

    option = input("Seleccione una opción: ")

    if option == "a":
        print("\n--- Crear Estudiante ---")
        print("i. Añadir Propiedades")
        print("ii. Subir al Servidor")
        print("iii. Regresar al menú principal")


        sub_option = input("Seleccione una opción: ")

        if sub_option == "i":
            create_student()
        elif sub_option == "ii":
            print("Subiendo información al servidor...")
            # Código para subir información al servidor
            print("Información subida exitosamente.")
        elif sub_option == "iii":
            continue
        else:
            print("Opción inválida.")

    elif option == "b":
        print("\n--- Mostrar estudiantes añadidos a la nube ---")
        show_students()

    elif option == "c":
        break
    else:
        print("Opción inválida.")
