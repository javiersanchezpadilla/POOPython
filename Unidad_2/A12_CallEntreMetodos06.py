""" Solución"""

class RobotCocina:
    def __init__(self, modelo):
        self.modelo = modelo
        self.energia = True

    def __preparar_masa(self):
        print("Mezclando y amasando la base...")

    def __poner_ingredientes(self):
        print("Añadiendo salsa y queso...")

    def __hornear(self):
        print("Horneando a 200°C...")

    def preparar_pizza(self):
        if self.energia:
            print(f"--- {self.modelo} iniciando pedido ---")
            self.__preparar_masa()       # Llamada interna 1
            self.__poner_ingredientes()  # Llamada interna 2
            self.__hornear()             # Llamada interna 3
            print("¡Proceso completado!")
        else:
            print("Error: Robot sin energía.")


bot = RobotCocina("ChefBot-3000")
bot.preparar_pizza()
