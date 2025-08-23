

# Ruta del archivo que contiene los datos
file_path = 'sesion12/info.txt'

# Lista para almacenar los diccionarios de usuarios y contraseñas
usuarios_y_contraseñas = []

# Abrir el archivo y leer línea por línea
with open(file_path, 'r') as file:
    lines = file.readlines()
    
    # Inicializar variables
    usuario = None
    contraseña = None
    
    for line in lines:
        # Limpiar la línea de espacios y saltos de línea
        line = line.strip()

        if line.startswith("User:"):
            # Si encontramos una línea con "User:", extraemos el usuario
            usuario = line.replace("User:", "").strip()
        
        elif line.startswith("Contraseña:"):
            # Si encontramos una línea con "Contraseña:", extraemos la contraseña
            contraseña = line.replace("Contraseña:", "").strip()

            # Si tanto usuario como contraseña están definidos, agregamos al diccionario
            if usuario and contraseña:
                usuarios_y_contraseñas.append({'usuario': usuario, 'contraseña': contraseña})
                usuario = None  # Reiniciar usuario para la siguiente entrada
                contraseña = None  # Reiniciar contraseña para la siguiente entrada

# Mostrar la lista de diccionarios con los usuarios y contraseñas
print(usuarios_y_contraseñas)
