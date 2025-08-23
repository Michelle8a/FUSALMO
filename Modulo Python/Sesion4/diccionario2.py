persona = {
    "nombre": "Karina",
    "edad": 26,
    "ciudad": "San Salvador"
}


print(persona["nombre"])  # Karina
print(persona["edad"])    # 26


persona["telefono"] = "1234-5678"  # agregamos un nuevo dato
persona["edad"] = 25               # cambiamos la edad


for clave, valor in persona.items():
    print(f"{clave} -> {valor}")


