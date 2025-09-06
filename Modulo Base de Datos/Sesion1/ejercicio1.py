#pip install requests
import requests

def buscar_pais():
    nombre_pais = input("Ingrese el nombre del país: ")
    url = f"https://restcountries.com/v2/name/{nombre_pais}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()[0]
        
        while True:
            print("\n--- Menú de opciones ---")
            print("1. Mostrar Datos generales")
            print("2. Mostrar Datos demográficos")
            print("3. Volver al menú principal")
            
            opcion = input("Ingrese una opción: ")
            
            if opcion == "1":
                mostrar_datos_generales(data)
            elif opcion == "2":
                mostrar_datos_demograficos(data)
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    else:
        print("No se encontró el país. Por favor, intente nuevamente.")
        
def mostrar_datos_generales(data):
    nombre = data["name"]
    bandera = data["flags"]
    poblacion = data["population"]
    
    print(f"\nNombre del País: {nombre}")
    print(f"URL de Bandera: {bandera}")
    print(f"Población Total: {poblacion}")

def mostrar_datos_demograficos(data):
    latitud = data["latlng"][0]
    longitud = data["latlng"][1]
    region = data["region"]
    subregion = data["subregion"]
    
    print(f"\nLatitud: {latitud}")
    print(f"Longitud: {longitud}")
    print(f"Región: {region}")
    print(f"Subregión: {subregion}")

def mostrar_todos_los_paises():
    url = "https://restcountries.com/v2/all"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        for pais in data:
            nombre = pais["name"]
            print(nombre)
    else:
        print("No se pudo obtener la lista de países. Por favor, intente nuevamente.")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Buscar País")
        print("2. Mostrar todos los países")
        print("3. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            buscar_pais()
        elif opcion == "2":
            mostrar_todos_los_paises()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
