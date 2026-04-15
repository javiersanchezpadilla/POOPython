""" HERENCIA Herencia sin constructor en la subclase 

    En este ejemplo, la clase Empleado no tiene un método __init__ definido.
    Sin embargo, al crear una instancia de Empleado, se llama automáticamente
    al constructor de la clase Persona, lo que permite inicializar el atributo 
    nombre sin necesidad de definir un constructor específico en Empleado. 
    Esto demuestra que la herencia en Python permite que las subclases 
    utilicen el constructor de la clase padre si no definen el suyo propio.

    El Sistema de Empleados
    -----------------------
    En este caso, la clase Persona configura el nombre. La clase Empleado 
    no tiene constructor propio, así que cuando creamos un empleado, Python 
    busca automáticamente el __init__ del padre.
    """
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Constructor de Persona ejecutado para: {self.nombre}")

class Empleado(Persona):
    # No hay __init__ aquí
    def trabajar(self):
        print(f"{self.nombre} está trabajando ahora mismo.")

# Al instanciar, pasamos el nombre que requiere el padre
sujeto = Empleado("Javier")
sujeto.trabajar()
