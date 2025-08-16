import re

#Validar DUI
dui = input("Escriba su numero de DUI: ")
regex = re.compile(r'^\d{8}-\d$')  #8 digitos-un digito
validacion = bool(regex.fullmatch(dui))

print(f"Tu dui es {dui}  Validacion: {validacion}")



#Validar NIT
dui = input("Escriba su numero de NIT: ")
validar_nit = re.compile(r'^\d{4}-\d{6}-\d{3}-\d$')
validacion2 = bool(validar_nit.fullmatch(dui))

print(f"Tu dui es {dui}  Validacion: {validacion2}")



#Validar email
email = input("Escriba su correo: ")
validar_email = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
validacion3 = bool(validar_email.fullmatch(email))

print(f"Correo: {email}  Validacion: {validacion3}")