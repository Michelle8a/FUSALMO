import impuestos as imp
import descuentos as des
from producto import productos
 
def calcular_precio_total(lista_productos):
 
    total = 0
 
    for producto in lista_productos:        
        total += productos[producto]
 
    tasa = imp.calcular_impuestos(total, imp.tasa)
    print(f"Porcentaje de Tasa de impuesto: {imp.tasa*100:.2f}%")
    print(f"Tasa a pagar: ${tasa:.2f}")
    subtotal = total + tasa
    print(f"Subtotal: ${subtotal:.2f}")
 
    descuento = des.calcular_descuentos(subtotal, des.descuento)
    print(f"Porcentaje de descuento: {des.descuento:.2f}%")
    print(f"Descuento realizado: ${descuento:.2f}")
    subtotal = subtotal - descuento
 
    return subtotal
 
 