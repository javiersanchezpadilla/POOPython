""" AGEGACION CONTRA COMPOSICIÓN

    Ahora comparemos la agregación con otro tipo de asociación: la composición.
    La composición implica definir objetos que están compuestos de otros 
    objetos.
    Inicialmente, estos dos conceptos pueden parecer muy similares porque ambos 
    implican la creación de objetos más complejos haciendo referencia a objetos 
    de otras clases.
    Pero tienen una diferencia clave

    AGREGACIÓN
    ==========
    La agregación es una relación de "tiene un".
    Una instancia de clase B tiene una instancia de clase A pero ambas pueden 
    existir de forma independiente.
    Si el programa elimina la instancia de la clase B, la instancia de la 
    clase A aún puede existir por sí sola, en el ejemplo A21_agregacion01.py
    la instancia (el objeto) 'carrito01' puede existir aunque 'emplado01' no 
    exista

        # Creamos un simple objeto
        carrito01 = Vehiculo("White", "XYZ 123", es_electrico=False)

        # Pasamos el objeto como argumento al objeto que lo “tendrá”
        empleado01 = Empleado("Jorge", carrito01)


    COMPOSICIÓN.
    ============
    En composición, un objeto compuesto no puede existir sin el objeto 
    que lo contiene.
    Por ejemplo, digamos que conceptualmente, una instancia de 'MotorAuto' no 
    puede existir sin su instancia de 'Automovil' en un programa determinado. 
    Si eliminamos la instancia 'Automovil' del programa, la instancia asociada 
    al automóvil 'MotorAuto' también debería eliminarse.
    
    Implementación:
    ---------------
    Para implementar esto en nuestro código, implicaría crear la instancia del 
    objeto compuesto dentro del objeto que lo contiene.
    De esta manera, cuando el objeto 'contenedor' se elimina del programa, el 
    objeto compuesto también se elimina.
    Como ejemplo usaremos el programa antes usado en el ejemplo 
    A21_Agregacion01.py, pero bajo el concepto de composición.

    Pero claro, esto depende de cómo representemos las asociaciones entre los 
    objetos en nuestro programa.
    Es importante comprender esta diferencia tanto en teoría como en la 
    práctica cuando implementas tu código.
"""

class Vehiculo:

    def __init__(self, color, placas, es_electrico):
        self.color = color
        self.placas = placas
        self.es_electrico = es_electrico

    def muestra_placa(self):
        print(self.placas)

    def muestra_info(self):
        print("Mi carrito:")
        print(f"Color: {self.color}")
        print(f"Placas: {self.placas}")
        print(f"Electrico: {self.es_electrico}")


class Empleado:
                       # he puesto vehiculo para hacer saber que aqui
                       # se colocará una instancia de Vehiculo 
    def __init__(self, nombre):
        self.nombre = nombre
                        # Creamos una instancia de la clase 'Vehiculo'
                        # dentro de la instancia de la clase 'Empleado'
                        # Esta instancia de 'Vehiculo' no puede existir
                        # sin la instancia de 'Empleado' que la contiene
        self.vehiculo = Vehiculo("White", "XYZ 123", es_electrico=False)
        # 👆🐷💀💩🦜🪿🐸🐠🐝 👆🐷💀💩🦜🪿🐸🐠🐝 👆🐷💀💩🦜🪿🐸🐠🐝

    def muestra_info_vehiculo(self):
        self.vehiculo.muestra_info()



empleado01 = Empleado("Jorge")

print(empleado01.nombre)
print(empleado01.vehiculo)
# Podemos de forma indirecta llamar a los métodos de la instancia agregada
# sin el intermediario del nombre de la instancia
empleado01.muestra_info_vehiculo()

# Llamando atributos indirectamente
print(empleado01.vehiculo.color)
print(empleado01.vehiculo.placas)
print(empleado01.vehiculo.es_electrico)

# Llamando metodos de forma indirecta
empleado01.vehiculo.muestra_placa()



