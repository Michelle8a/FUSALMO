from producto import productos
from calcular_precio import calcular_precio_total
import os
def mostrar_menu():

    os.system("cls")
    
    print("Bienvenido a la tienda en línea.")
    print("Productos disponibles:")

    for producto, precio in productos.items(): #llamo el diccionario de productos
        #.items separa las variables del diccionario
        print(f"{producto}: ${precio:.2f}")
    
    print("Ingrese los productos que desea comprar separados por comas (ejemplo: manzanas, naranjas, peras) o escriba 'salir' para salir.")
    
    productos_compra = input("> ").lower() #meto los productos que escribi en una variable
    
    if productos_compra == "salir": #para salir
        return None
    
    lista_productos_compra = productos_compra.split(",") #checa donde estan las comas y convierte la cadena en una lista
    
    for producto in lista_productos_compra: #checa si los productos que escribi estan en la lista
        
        if producto.strip() not in productos: #.strip elimina los espacios al inicio y al final

            print(f"{producto.strip()} no está en la lista de productos disponibles.")

            return None
    
    return lista_productos_compra

def main():
    
    while True:
        
        lista_productos_compra = mostrar_menu()
        
        if lista_productos_compra is None:
            break
        
        print("Productos: ", lista_productos_compra, type(lista_productos_compra))
        
        precio_total = calcular_precio_total(lista_productos_compra)
        
        print(f"El precio total de la compra es: ${precio_total:.2f}")
        
        input()

if __name__ == "__main__":
    main()