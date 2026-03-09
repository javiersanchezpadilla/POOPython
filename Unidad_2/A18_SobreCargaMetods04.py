""" Este ejercicio ayudará a entender cómo un solo método puede ser 
    "inteligente" y adaptarse a lo que el usuario le entregue.

    Vamos a diseñar el método configurar para una clase Personaje. 
    El reto es que el mismo método debe funcionar en tres escenarios distintos.
    
    Escenario: El Creador de Héroes
    Queremos que nuestra clase Personaje sea flexible. El método configurar
    recibirá datos, pero no siempre recibirá todos.
    
    Puntos clave:
    A)  El valor None es nuestro aliado: Usamos None como "marcador de posición" 
        para saber si el usuario envió algo o no.
    B)  Argumentos por Nombre (Keywords): Nota que en las pruebas puse vida=150. 
        Esto es genial en Python porque permite saltarse el orden de los 
        parámetros si el método tiene muchos.
    C)  Limpieza del código: En lugar de tener 3 métodos (configurar_vida, 
        configurar_arma, configurar_todo), tenemos uno solo que centraliza 
        la lógica.

    Reto rápido para los alumnos:
    Pedir que modifiquen el código para añadir un tercer parámetro opcional 
    llamado escudo.
    La pregunta para ellos sería: > "Si un personaje ya tiene 100 de vida y le 
    configuran un escudo de 50, ¿debería el método sumar ambos valores en un nuevo 
    atributo self.defensa_total o guardarlos por separado?"
"""

class Personaje:
    def __init__(self, nombre_inicial="Desconocido"):
        self.nombre = nombre_inicial
        self.vida = 100        # Valor por defecto
        self.arma = "Puños"    # Valor por defecto

                                                    # MÉTODO "SOBRECARGADO" (Adaptable)
    def configurar(self, vida=None, arma=None):
                                                    # Escenario 1: Solo recibimos Vida
        if vida is not None and arma is None:
            self.vida = vida
            print(f"{self.nombre}: Vida actualizada a {self.vida}")
            
                                                    # Escenario 2: Solo recibimos Arma
        elif vida is None and arma is not None:
            self.arma = arma
            print(f"{self.nombre}: Ahora porta un {self.arma}")
            
                                                    # Escenario 3: Recibimos ambos
        elif vida is not None and arma is not None:
            self.vida = vida
            self.arma = arma
            print(f"{self.nombre} EQUIPADO: {self.vida} HP y {self.arma}")
            
                                                    # Escenario 4: No recibimos nada
        else:
            print(f"{self.nombre} no ha cambiado su equipo.")


hero = Personaje("Arturo")

hero.configurar(vida=150)                           # Solo vida
hero.configurar(arma="Espada Láser")                # Solo arma
hero.configurar(200, "Escudo Real")                 # Ambos (por posición)
hero.configurar(arma="Machete", vida=90)            # Ambos por referencia
hero.configurar()                                   # Nada
