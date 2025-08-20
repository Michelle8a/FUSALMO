import datetime as dt
class Persona:

    def __init__(self, nombres, apellidos, fecha, sexo, edad):
        self.nombre = nombres
        self.primer_nombre = nombres.split(" ")[0]
        self.apellido = apellidos
        self.primer_apellido = apellidos.split(" ")[0]
        self.fecha_nacimiento = fecha
        self.sexo = sexo
        self.edad = self.calcular_fecha(fecha)

    def saludar(self):

        genero = "una niña" if self.sexo == "niña" else "un niño"

        '''
        if self.sexo == "niña":
            genero = "una niña"
        elif self.sexo == "niño":
            genero = "un niño"
        '''
    
        print(f"Hola mi nombre es {self.nombre} tengo {self.edad} años de edad y soy "+ genero)

    def comer(self):
        print(f"{self.primer_nombre} esta comiendo")
    
    def dormir(self):
        print(f"{self.primer_nombre} esta durmiendo")
    
    
    def calcular_fecha(fecha_nacimiento):

        #paso el string a formato datetime
            formato_fecha = "%d/%m/%Y"
            fecha= dt.datetime.strptime(fecha_nacimiento, formato_fecha) 
            
            hoy = dt.datetime.now() #agarro la fecha de hoy
            edad = hoy.year - fecha.year

            if (hoy.month, hoy.day) < (fecha.month, fecha.day):
                edad -= 1

            return edad


    