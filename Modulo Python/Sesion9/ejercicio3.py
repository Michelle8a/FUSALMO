import datetime

entrada = input("Ingrese la hora de entrada en formato HH:MM ")
hora_entrada = datetime.datetime.strptime(entrada, "%H: %M")

salida = input("Ingrese la hora de salida en formato HH:MM ")
hora_salida = datetime.datetime.strptime(salida, "%H: %M")

#Calcular las horas trabajadas

if hora_salida > hora_entrada:
    horas_trabajadas = hora_salida - hora_entrada


horas = horas_trabajadas.total_seconds() / 3600
minutos = (horas % 1) + 60

print(f"El trabajador trabajo {horas:.0f} horas y {minutos:.0f} minutos")