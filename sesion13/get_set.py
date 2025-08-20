
class videoGame:

    def __init__(self, plataforma, genero):
        self.plataforma = plataforma
        self.genero = genero


    def set_plataforma(self, plataforma):
        self.plataforma = plataforma

    def get_plataforma(self, plataforma):
        return self.plataforma
    

    def set_genero(self, genero):
        self.genero = genero

    def get_genero(self, genero):
        self.genero = genero


juegoSteam = videoGame("PC", "Zombies")
print(f"Mi juego se utiliza en {juegoSteam.get_plataforma()}")

juegoSteam.set_plataforma("Playstation 5")
print(f"Mi juego se utiliza en {juegoSteam.get_plataforma()}")