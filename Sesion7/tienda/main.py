from producto import productos
from calcular_precio import calcular_precio_total
import os
def mostrar_menu():

    os.system("cls")
    
    print("Bienvenido a la tienda en línea.")
    print("Productos disponibles:")

    for producto, precio in productos.items():
        
        print(f"{producto}: ${precio:.2f}")
    
    print("Ingrese los productos que desea comprar separados por comas (ejemplo: manzanas, naranjas, peras) o escriba 'salir' para salir.")
    
    productos_compra = input("> ").lower()
    
    if productos_compra == "salir":
        return None
    
    lista_productos_compra = productos_compra.split(",")
    
    for producto in lista_productos_compra:
        
        if producto.strip() not in productos:
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