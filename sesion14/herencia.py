class persona:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

    def print_name(self):
        print(self.nombres, self.apellidos)

class animal:
    def saludo(self):
        return "Saludos"

class estudiante(persona, animal):
    def __init__(self, nombres, apellidos, edad):
        self.edad = edad
        persona.__init__(self, nombres, apellidos)




manu = persona("Karina", "Ochoa")
manu.print_name()


jose = estudiante("Jose", "Gonzalez", 24)
jose.print_name()


pedro = estudiante("Pedro", "Fernandez", 25)
pedro.print_name()
print(pedro.saludo())