
class carro:
    año_fabrica = 2023
    marca = ""
    modelo = ""

miCarro = carro()
miCarro.año = 2015
print(miCarro.año)
print(type(miCarro))

carro_hermano = carro()
carro_hermano.año = 2012
carro_hermano.marca = "Mitsubishi"
print(carro_hermano.año)
print(carro_hermano.marca)