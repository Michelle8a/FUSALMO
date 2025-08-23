nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (M para mujer, H para hombre): ").upper()
edad = int(input("Ingrese su edad: "))


if genero == "H" and edad >= 18:
    grupo = 1
    turno = "Mañana"

elif genero == "M"  and edad >= 18:
    grupo = 2
    turno = "Mañana"

elif genero == "H" and edad <= 18:
    grupo = 1
    turno = "Tarde"

elif genero == "M" and edad <= 18:
    grupo = 2
    turno = "Tarde"

print(f"\nINFORMACION")
print(f"Nombre: {nombre} \nGenero: {genero} \nEdad: {edad} ")
print(f"Turno: {turno} \nGrupo: {grupo}")