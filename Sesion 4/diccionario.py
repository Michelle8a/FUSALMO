import os
datos = ["Nombre", "Edad", "Nacionalidad", "Lenguaje de programación favorito"]
personas = []
 
while True:
 
    os.system("cls")
    print("Menu:")
    print("1. Añadir nueva persona")
    print("2. Mostrar personas")
    print("3. Actualizar datos de personas")
    print("4. Salir")
 
    opcion = input("Seleccione una opción: ")
 
    if opcion == "1":
 
        nueva_persona = {}        
        for dato in datos:
            valor = input(f"Ingrese {dato}: ")
            nueva_persona[dato] = valor
 
        personas.append(nueva_persona)
 
    elif opcion == "2":
 
        if len(personas) == 0:
            print("No hay personas registradas.")
 
        else:
            i = 1
            for persona in personas:
 
                print(f"Persona {i}:")
                for clave, valor in persona.items():
                    print(f"{clave}: {valor}")
 
                i += 1
    elif opcion == "3":
        if len(personas) == 0:
            print("No hay personas registradas para actualizar.")
        else:
            indice = int(input("Ingrese el número de la persona a actualizar (1 para la primera): ")) - 1
           
            for dato in datos:
                valor = input(f"Ingrese nuevo {dato} (deje en blanco para no cambiar): ")
                if valor:
                    personas[indice][dato] = valor
            print("Datos actualizados.")
           
    elif opcion == "4":
        print("Saliendo del programa...")
        break
 
    input("Presione Enter para continuar...")