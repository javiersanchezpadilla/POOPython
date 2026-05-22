""" MULTIPLES CONTEXT MANAGERS

    ¿Podemos usar with para múltiples archivos separados por comas?
    ---------------------------------------------------------------
    Sí, se puede usar with para múltiples archivos separados por comas, y es 
    una práctica muy recomendada porque hace el código más limpio y legible.

    Nota: solo funciona de la version de Python 3.1 en adelante

    ¿Qué pasa aquí?
    ---------------

    **) Se abren dos archivos en la misma línea
    **) Se separan por coma (`,)
    **) Cada uno tiene su propia variable (archivo1 y archivo2)
    **) Al salir del bloque with, ambos se cierran automáticamente

"""
with open("datos2.txt", "r") as archivo1, open("datos3.txt", "w") as archivo2:
    contenido = archivo1.read()
    archivo2.write(contenido)
    # Ambos archivos se cierran automáticamente al salir
