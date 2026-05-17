""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Agregar información al final de un archivo
"""

with open("notas.txt", "a") as archivo:
    archivo.write("Hola alumnos.")
    # Podemos hacer loque deseemos aquí adentro...
    # En cuanto el código sale de la sangría (tabulación), 
    # Python cierra el archivo automáticamente detrás de escena.

print("El archivo ya está cerrado aquí.")
