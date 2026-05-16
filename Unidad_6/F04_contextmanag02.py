""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON"""

with open("notas.txt", "w") as archivo:
    archivo.write("Hola alumnos.")
    # Podemos hacer loque deseemos aquí adentro...
    # En cuanto el código sale de la sangría (tabulación), 
    # Python cierra el archivo automáticamente detrás de escena.

print("El archivo ya está cerrado aquí.")