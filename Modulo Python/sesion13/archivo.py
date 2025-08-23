import os

os.system('cls')

file_path = 'sesion12/demofile.txt'

file = open(file_path, "a", encoding=("utf-8"))
file.write("\nHola como estan")
file.close()


file = open(file_path, "r", encoding=("utf-8"))
print(file.read())
file.close()


file = open(file_path, "w", encoding=("utf-8")) #Borra todo el contenido del documento y empieza a escribir
file.write("\nHola como estan")
file.close()

open("sesion13/bitacora.txt", "a")
os.remove("sesion13/bitacora.txt") #Borra el arcvhico

existe = os.path.exists("sesion13/bitacora.txt")
if existe:
    print("El archivo existe")

else:
    print("El archivo no existe")

print(os.getcwd())

#print(os.path.abspath(_file_))
print(os.system("dir"))#Ver carpetas actuales



os.mkdir("Lista de incidentes") #Crear carpetas
os.rmdir("Lista de incidentes") #Eliminar carpetas
