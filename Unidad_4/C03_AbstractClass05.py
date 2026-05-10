""" CLASES ABSTRACTAS Y MÉTODOS ABSTRACTOS 

    ¿Son lo mismo?
    No son lo mismo, pero están íntimamente relacionados.
    LA clase Abstracta es el 'contenedor' o el 'plano completo', y los 
    Métodos Abstractos son las 'piezas faltantes' que obligatoriamente 
    alguien más debe fabricar.

    Diferencias técnicas:

    1. La Clase Abstracta (El Contenedor)
    -------------------------------------
    Es una clase que hereda de ABC. Su característica principal es que no 
    permite crear objetos (instancias) de ella.

    A)  ¿Puede tener lógica real? Sí, Puede tener métodos normales (con 
        código) que todos los hijos heredarán y usarán igual. Esto sirve para 
        reutilizar código.

    B)  En el ejemplo del programa anterior, en la clase Sensor, el método 
        __init__ que guarda el nombre es lógica real. No es abstracto, porque 
        todos los sensores guardan su nombre de la misma forma.

    2. El Método Abstracto (La Obligación)
    --------------------------------------
    Es una función dentro de esa clase que tiene el decorador @abstractmethod.

    A)  ¿Tiene lógica? Normalmente no tiene código (solo lleva un pass).
    B)  Su función: Es una 'promesa', nos dice 'No sé cómo se hace esto todavía, 
        pero te juro que cualquier hijo mío sabrá hacerlo".
    C)  Su impacto: Si una clase tiene al menos un método abstracto, la clase 
        se vuelve abstracta automáticamente y no se puede instanciar.

        
    Elemento            ¿Puede tener código?        ¿Qué le hace a la clase?
    --------------------------------------------------------------------------
    Clase Abstracta     Sí, puede tener métodos     Evita que se creen objetos 
                        completos y atributos.      Base().
    Método Abstracto    No (normalmente),           solo Obliga a las subclases 
                        define el nombre.           a escribir su propia versión.

    Ejemplo para comparar ambos en una sola clase:
    Observar y entendera cómo conviven la lógica real y la abstracción:

    LAS CLASES ABSTRACTAS OBLIGAN EL POLIMORFISMO.
    Este ejemplo contiene lógica de programación dentro de la clase abstracta
"""
from abc import ABC, abstractmethod

class PersonajeJuego(ABC):                      # <-- CLASE ABSTRACTA
    def __init__(self, nombre):
        # LÓGICA REAL: Todos los personajes tienen nombre, 
        # no hace falta que cada hijo repita este código.
        self.nombre = nombre
        self.energia = 100

    def recibir_daño(self, cantidad):
        # LÓGICA REAL: El daño se resta igual para todos.
        self.energia -= cantidad
        print(f"{self.nombre} ahora tiene {self.energia} de energía.")

    @abstractmethod
    def habilidad_especial(self):               # <-- MÉTODO ABSTRACTO
        # SIN LÓGICA: El padre no sabe qué hace cada uno.
        # Obliga al hijo a definirlo.
        pass


class Guerrero(PersonajeJuego):
    def habilidad_especial(self):
        print(f"{self.nombre} usa !GOLPE DE ESPADA!")

# --- PRUEBA ---
g = Guerrero("Aragorn")
g.recibir_daño(20)      # Usa lógica real heredada del padre.
g.habilidad_especial() # Usa la lógica que él mismo implementó por obligación.
