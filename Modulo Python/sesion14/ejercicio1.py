'''
Crear una clase animal que herede en 3 sub clases diferentes
almenos 3 metodos y 3 propiedades

'''

class Animal:

    def __init__(self,nombre, raza, color, sonido):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.sonido = sonido

    
    def hacer_sonido(self):
        print(f"{self.nombre} hace {self.sonido}")

    def moverse(self):
        print(f"{self.nombre} se esta moviendo")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")

    


class Perro(Animal):
    def correr(self):
        print(f"{self.nombre} esta corriendo")

    def hacer_truco(self):
        print(f"{self.nombre} esta haciendo un truco")


class Gato(Animal):
    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def ronronear(self):
        print(f"{self.nombre} esta ronroneando")


class Pollo(Animal):
    def picotear(self):
        print(f"{self.nombre} esta picoteando")

    def poner_huevo(self):
        print(f"{self.nombre} puso un huevo")   


perro = Perro("Firulais", "Pitbull", "Cafe", "Guau")
gato = Gato("Michi", "Persa", "Gris", "Miau")
pollo = Pollo("Clotilde", "Gallina blanca", "Blanca", "Pioo")



perro.mostrar_info()
print()
gato.ronronear()
print()
pollo.hacer_sonido()
pollo.poner_huevo()