""" Ejemplo del encadenamiento (Method Chaining Example)

    En este ejemplo, tenemos la clase Pizza y la instancia pizza
    a la cual agregaremos ingredientes
"""

class Pizza:
 
   def __init__(self):
       self.cubierta = []
 
   def agregar_cubierta(self, ingrediente):
       self.cubierta.append(ingrediente.lower())
                        # Esta última linea es lo que permite el encadenamiento
       return self      # ya que retorna 'self' (la referencia a la instancia)
                        # que llamo al método), de esta manera es que podemos llamar
                        # otro método en la misma linea en una secuencia
 
   def muestra_cubierta(self):
       print("Esta pizza tiene:")
       for ingrediente in self.cubierta:
           print(ingrediente.capitalize())

pizza = Pizza()
print('\nFORMA 1')
pizza.agregar_cubierta("champiñones").agregar_cubierta("olivas").agregar_cubierta("pollo").muestra_cubierta()

# Para facilitar la lectura del código, se puede escribir la llamada del método 
# en varias lineas usando ( \ ) para indicar que la siguiente línea es continuación 
# de la actual linea.
print('\nFORMA 2')
pizza.agregar_cubierta("champiñones") \
    .agregar_cubierta("olivas") \
    .agregar_cubierta("pollo") \
    .muestra_cubierta()

# También es posible envolver las líneas entre paréntesis:
print('\nFORMA 3')
(pizza.agregar_cubierta("champiñones") \
    .agregar_cubierta("olivas") \
    .agregar_cubierta("pollo") \
    .muestra_cubierta())
