""" MULTIPLES CONTEXT MANAGER

    Con comas vs Sin comas
"""
with open("datos2.txt", "r") as fuente:
    with open("datos5.txt", "w") as destino:
        destino.write(fuente.read())
    # Mucha indentación
