""" GENERADORES (YIELD).

    En este ciclo agotamos todos los valores del generador, en el caso del 
    ciclo 'for' no hacer falta indicar la instrucción <next> ya que esta de 
    forma automática implícita el comando dentro del ciclo.
"""
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

# utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador:{generador}')
print(type(generador))

for valor in generador:
    print(f'Numero producido: {valor}')
