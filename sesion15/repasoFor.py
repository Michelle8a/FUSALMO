'''
Crear un programa de python que ejecute las tbalas de multiplicar
del 1 al 10 de una vez
'''


for numero in range(1, 11): #del 1 al 10

    print(f"\nTabla de multiplicar del {numero}")
  
    for i in range(1, 11): 
        print(f"{numero} x {i} = {numero * i}")
