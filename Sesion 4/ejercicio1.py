'''
Diccionario de palabras con significado
agregar palabras, ver palabras, modificar y salir
'''

# Un diccionario para almacenar las palabras y sus significados.
diccionario = {}

while True:
    print("\n--- Menú de Opciones ---")
    print("1. Agregar palabra")
    print("2. Ver palabras")
    print("3. Modificar palabra")
    print("4. Salir")
    
    opcion = int(input("Elige una opción (1-4): "))

    if opcion == 1:
        # Agregar palabra
        palabra = input("Escribe la palabra que quieres agregar: ").title()
        if palabra in diccionario:
            print(f"'{palabra}' ya existe. Usa la opción de modificar si quieres cambiarla.")
        else:
            significado = input(f"Escribe el significado de '{palabra}': ").title()
            diccionario[palabra] = significado
            print(f"¡'{palabra}' ha sido agregada con éxito!")

    elif opcion == 2:
        # Ver palabras
        if not diccionario:
            print("El diccionario esta vacio.")
        else:
            print("\n--- Diccionario ---")
            for palabra, significado in diccionario.items():
                print(f"Palabra: {palabra}\nSignificado: {significado}\n" + "-"*15)

    elif opcion == 3:
        # Modificar palabra
        palabra = input("Escribe la palabra que quieres modificar: ").title()
        if palabra not in diccionario:
            print(f"'{palabra}' no se encuentra en el diccionario.")
        else:
            nuevo_significado = input(f"Escribe el nuevo significado para '{palabra}': ").title()
            diccionario[palabra] = nuevo_significado
            print(f"¡El significado de '{palabra}' ha sido modificado!")

    elif opcion == 4:
        # Salir
        print("¡Hasta luego!")
        break
    
    else:
        # Opción inválida
        print("Opcion no valida. Por favor, elige un numero del 1 al 4.")