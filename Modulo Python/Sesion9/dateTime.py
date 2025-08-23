import datetime
import locale

# Configurar el locale a español (El Salvador, por ejemplo)
locale.setlocale(locale.LC_TIME, "es_SV.UTF-8")  # o "es_ES.UTF-8" para España


x = datetime.datetime.now() 
print(x) #muestra fecha y hora
print(x.year) 
print(x.strftime("%A")) #Dia de la semana


y = datetime.datetime(1999, 3, 16) #año, mes, dia
print(y)
print(y.strftime("%A"))