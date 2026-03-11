""" Reto de progamación

    A este proceso en programación se le llama Refactorización. El objetivo 
    es tomar un método "espagueti" (largo y difícil de leer) y dividirlo en 
    piezas pequeñas, como si fueran bloques de LEGO, que se llaman entre sí.

    observen lo difícil que es leer el método preparar_pizza porque hace 
    demasiadas cosas al mismo tiempo:

    El Reto: "Divide y Vencerás" (15 min)
    Pide a los equipos que reescriban la clase siguiendo estas instrucciones:

    Crear 3 métodos de apoyo (privados):
    ------------------------------------
    1)  __preparar_masa(self)
    2)  __poner_ingredientes(self)
    3)  __hornear(self)

    Limpiar el método principal: El método preparar_pizza(self) ahora solo debe 
    contener 3 líneas de código, llamando a los métodos anteriores usando self..

    Añadir una validación: El método preparar_pizza solo debe iniciar si el robot 
    tiene energía (pueden agregar un atributo self.energia = True).

    Está es la versión para la practica, la respuesta es el proximo código

    Pregunta para pensar:
    ---------------------
    ¿Qué pasa si ahora el cliente quiere una Calzone en lugar de una Pizza?"
    Respuesta: Solo tendríamos que crear un método preparar_calzone que reutilice 
    __preparar_masa y __hornear, cambiando solo los ingredientes. 

"""

class RobotCocina:
    def __init__(self, modelo):
        self.modelo = modelo

    def preparar_pizza(self):
                                                # Paso 1: Masa
        print("Mezclando harina y agua...")
        print("Amasando por 5 minutos...")
                                                # Paso 2: Ingredientes
        print("Añadiendo salsa de tomate...")
        print("Esparciendo queso mozzarella...")
                                                # Paso 3: Horneado
        print("Calentando horno a 200 grados...")
        print("Horneando por 15 minutos...")
        print("¡Pizza lista!")


bot = RobotCocina("ChefBot-3000")
bot.preparar_pizza()
