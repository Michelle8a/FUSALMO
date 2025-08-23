
class car:

    def move(self):
        return "Se conduce"
    
class plane:

    def move(self):
        return "Se planea"
    
class boat:

    def move(self):
        return "Se navega"
    

carro1 = car()
avion1 = plane()
bote1 = boat()

for x in (carro1, avion1, bote1):
    print(x.move())