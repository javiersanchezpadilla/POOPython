""" MULTIPLES CONTEXT MANAGER

    cuándo es mejor NO usar comas
"""
                            # Si cada archivo necesita su propio manejo de 
                            # errores
try:
    with open("archivo1.txt", "r") as f1:
        datos1 = f1.read()
except FileNotFoundError:
    datos1 = "predeterminado"

try:
    with open("archivo2.txt", "r") as f2:
        datos2 = f2.read()
except FileNotFoundError:
    datos2 = "vacío"

                            # Aquí NO conviene usar comas porque los errores 
                            # se manejan por separado
