'''
Crear una clase que tenga los siguientes atributos
Nombres, apellidos, fecha de nacimiento, sexo, edad
la edad debe calcularse a partir de la fecha de nacimiento

Metodos:
-Saludar    "Hola mi nombre es _ tengo tantos años de edad y soy un {niño/niña}
-Dormir     Mensaje de dormir
-Comer      Mensaje de comer
'''

import persona as p

fecha = input("Escriba su fecha de nacimiento (dd/mm/aaaa): ")

nombres = input("Escriba sus nombres: ").title()
apellidos = input("Escriba sus apellidos: ").title()

sexo = input("Escriba su sexo: ").lower()


persona = p.Persona(nombres, apellidos, fecha, sexo)

p.Persona.saludar(persona)
p.Persona.comer(persona)
p.Persona.dormir(persona)

#tambien se puede de est manera si la funcion no imprime y es un return
print(persona.saludar())


