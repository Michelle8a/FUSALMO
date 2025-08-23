
agenda = []

def agregar_contacto(nombre, telefono):
    '''
     for contacto in agenda:
        
        if contacto["Nombre"].lower() == nombre.lower():
            print("El contacto ya existe")
            break
    '''
      
    agenda.append({"Nombre": nombre, "Telefono": telefono})
    print("Contacto agregado")
 

def mostrar_agenda():

    if len(agenda) == 0:
        print("La agenda esta vacia")
    
    else:
        for contacto in agenda:
            print(f"Nombre: {contacto["Nombre"]} - Telefono: {contacto["Telefono"]}")


def buscar_contacto(nombre):

    busqueda = []

    for contacto in agenda:

        if nombre in contacto["Nombre"]:
            busqueda.append(busqueda)

        if len(busqueda) > 0:
            i = 0
            for contacto in busqueda:
                i += 1
                print(f"{i}. Nombre: {contacto["Nombre"]} - Telefono: {contacto["Telefono"]}")
        
    return f"{nombre} no esta en la agenda"


def eliminar_contacto(nombre):

    for contacto in agenda:

        if contacto["Nombre"].lower() == nombre.lower():
            
            print("Contacto a eliminar")
            print(f"Nombre: {contacto["Nombre"]} - Telefono: {contacto["Telefono"]}")

            eliminar = input("Confirme para eliminar (y/n): ")

            if eliminar.lower() == "y":

                agenda.remove(contacto)
                print("Contacto eliminado")
            
            elif eliminar.lower() == "n":
                print("Cancelando")
            
            else:
                print("Elija una opcion valida")