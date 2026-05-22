""" MULTIPLES CONTEXT MANAGER

    Leer tres archivos y combinarlos
"""
with open("datos.txt", "r") as f1, \
     open("datos2.txt", "r") as f2, \
     open("datos3.txt", "r") as f3:
    
    contenido1 = f1.read()
    contenido2 = f2.read()
    contenido3 = f3.read()
    combinado = contenido1 + contenido2 + contenido3
    print(combinado)

print("Archivos leídos y cerrados automáticamente")
