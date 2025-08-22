
class Dominios:

    def __init__(self, reino ):
        self.reino = reino

    def set_definicion(self, definicion):
        self.definicion = definicion
        
    

class Animalia(Dominios):
    animales = []

    def agregar_animal(self, *animales): 
        #el * es para envial una lista indefinida
        for animal in animales:
            self.animales.append(animal)

    def get_animal(self):
        return self.animales



mamiferos = Dominios("Los mamiferos")
mamiferos.agregar_animal("Leon", "Gato", "Tigre")