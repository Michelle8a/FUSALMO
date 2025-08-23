import os
frutas = ["manzana", "banana", "naranja", "uva"]
 
while True:
    os.system('cls')
    print("Menu: ")
    print("1. Agregar fruta")
    print("2. Mostrar frutas")
    print("3. Eliminar frutas")
    print("4. Modificar frutas")
    print("5. Salir")
 
    opcion = int(input("Seleccione una opción: "))
 
    if opcion == 1:
        fruta = input("Ingrese el nombre de la fruta: ")
        frutas.append(fruta)
        print(f"{fruta} ha sido agregada a la lista.")
 
    elif opcion == 2:
        if len(frutas) > 0:
            print("Lista de frutas:")
            for f in frutas:
                print(f)
        else:
            print("No hay frutas en la lista.")
   
    elif opcion == 3:
        if len(frutas) > 0:
 
            fruta = input("Ingrese el nombre de la fruta a eliminar: ")
            if fruta in frutas:
               
                frutas.remove(fruta)
                print(f"{fruta} ha sido eliminada de la lista.")
 
            else:
                print(f"{fruta} no se encuentra en la lista.")
        else:
            print("No hay frutas en la lista para eliminar.")
 
    elif opcion == 4:
        if len(frutas) > 0:
            fruta = input("Ingrese el nombre de la fruta a modificar: ")
            if fruta in frutas:                
                index = frutas.index(fruta)
                nueva_fruta = input("Ingrese el nuevo nombre de la fruta: ")
                frutas[index] = nueva_fruta
 
                print(f"{fruta} ha sido modificada a {nueva_fruta}.")
            else:
                print(f"{fruta} no se encuentra en la lista.")
        else:
            print("No hay frutas en la lista para modificar.")
 
    elif opcion == 5:
        print("Saliendo del programa.")
        break
 
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
 
    input("----------")