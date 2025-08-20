

file = open("sesion12\demofile.txt", "r")

#Lee la linea completa hasta donde encuenta el salto de 
print(file.readline()) 

for line in file: #imprime todas las lineas, incluyendo el salto
    print(line)