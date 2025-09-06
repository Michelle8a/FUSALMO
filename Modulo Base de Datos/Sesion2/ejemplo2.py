
import net
import bcrypt

nombre_completo = input("Ingrese el nombre completo: ")
usuario = input("Ingrese el usuario")
contraseña = input("Ingrese la contraseña")

hashed = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt( ))

#Ejecutar consulta de insercion
sql = "INSERT INTO usuarios(nombre_completo, usuario, contraseña) VALUES (%s, %s, %s)"
val = (nombre_completo, usuario, contraseña)
net.mycursor.execute(sql, val)

#Confirmar la operacion
net.mydb.commit()

#Imprimir el usuario recien insertado
print(net.mycursor.lastrowid)