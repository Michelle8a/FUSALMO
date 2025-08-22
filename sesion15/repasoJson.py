
file = open("repaso.txt", "r") #leer
print(file.read())
file.close()

file = open("repaso.txt", "a") #agregar al final del documento
file.write("\nfinal_1")
file.write("\nfinal_2")
file.write("\nfinal_3")
file.write("\nfinal_4")
file.close()


file = open("repaso.txt", "w") #borra el contenido para sobreescribir
file.write("\nfinal_nuevo_1")
file.write("\nfinal_nuevo_2")
file.write("\nfinal_nuevo_3")
file.write("\nfinal_nuevo_4")
file.close()

try:
    file = open("repaso.txt", "x") #Crea un nuevo archivo si el archivo no existe
    file.write("\nTexto Nuevo")
    file.close()

except FileExistsError:
    print("El archivo ya existe")