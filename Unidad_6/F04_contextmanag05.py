""" MULTIPLES CONTEXT MANAGERS

    Copiar contenido de un archivo a otro
 """
with open("datos3.txt", "r") as fuente, open("datos4.txt", "w") as destino:
    destino.write(fuente.read())
    # Ambos se cierran automáticamente
