
class Carro:

    color = ""
    total_pasajeros = 0

    def __init__(self, year, brand, model): #constructor
        
        self.año_fabrica = year
        self.marca = brand
        self.modelo = model

    def __str__(self):
        return f"El año del carro es: {self.año_fabrica}"
    
    def andar(self): #Metodo
        print(f"Avanzando") 


