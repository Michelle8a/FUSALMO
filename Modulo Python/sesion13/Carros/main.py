import carro as car

miCarro = car.Carro(2013, "Kia", "Picanto")
print(miCarro.año_fabrica)
print(miCarro.marca)
print(miCarro.modelo)

miCarro.color = "Blanco"

print(miCarro)
miCarro.andar()

del miCarro.marca


