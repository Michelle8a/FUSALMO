
x = "hola"



#raise Exception("Mensaje de error")

#raise ZeroDivisionError("Division entre cero de ejemplo")

try:
    print(x)
    if not type(x) is int:
        raise TypeError("Solo se permiten enteros")

except NameError:
    print("Una variable no esta definida")

except:
    print("Ocurrio un error")

else:
    print("El sistema se ha ejecutado sin errores")

finally:
    print("Finalizando el sistema")