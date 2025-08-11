nombre = input("Ingrese su nombre: ")
cantidad = int(input("Ingrese la cantidad de productos: "))
total = float(input("Ingrese el total de la compra: "))

print(f"\nNombre del Cliente: {nombre}")
print(f"Cantidad de Productos Comprados: {cantidad}")

if cantidad >= 3 and total > 100:
    resultado = total - (total * 0.15)
    print(f"Su total con descuento es de ${resultado:.2f}")

elif cantidad >= 3 or total > 100:
    resultado = total - (total * 0.05)
    print(f"Su total con descuento es de ${resultado:.2f}")

else:
    print("No recibe ningun descuento")


