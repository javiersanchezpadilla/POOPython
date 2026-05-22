""" MULTIPLES CONTEXT MANAGER

    Leer de uno y escribir en dos
"""
with open("datos.txt", "r") as entrada, \
     open("salida1.txt", "w") as salida1, \
     open("salida2.txt", "w") as salida2:
    
    datos = entrada.read()
    salida1.write(datos.upper())
    salida2.write(datos.lower())
    # Los tres archivos se cierran automáticamente