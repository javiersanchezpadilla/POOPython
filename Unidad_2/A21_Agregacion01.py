""" AGREGACION

    Un empleado tiene un vehículo, Este vehículo podría ser asignado por la 
    empresa para realizar el trabajo o algo relacionado con ello, pero digamos 
    que en nuestro programa un empleado tiene un vehículo, por lo que tiene 
    una relación, define el concepto de agregación.
    La palabra 'tiene un' realmente define la relación de agregación de la 
    clase “A” dentro de la clase “B”
    Almacenaremos la información del vehículo dentro del empleado, pero serán 
    dos objetos separados en nuestro código.
    Simplemente los conectaremos o asociaremos en nuestro programa así tendremos 
    la clase vehículo y la clase empleado, por lo que serán objetos separados.
    Pero como empleado necesita la información del vehículo, trabajaremos con 
    el vehículo dentro de la clase empleado, es muy importante no olvidar que 
    siguen siendo clases separadas (vamos a definirlos por separado).
    No estamos escribiendo la información del vehículo directamente dentro del 
    empleado, los mantenemos separados, pero usamos un vehículo y lo guardamos 
    dentro del empleado.
    Cuando creamos instancias de cada una de estas clases, vehículo y empleado, 
    la instancia de empleado almacenará y contendrá una instancia de vehículo, 
    pero seguirán siendo objetos separados.

    Pero cuando creamos el empleado, vamos a pasar el vehículo, la instancia 
    como un argumento, y vamos a almacenarlo para que podamos usarlo dentro de 
    la clase de empleado.

    RESUMEN:
    -------
    La agregación se da cuando creamos dos instancias (objetos) independientes
    y en algún momento mandamos una instancia como argumento para la creación
    de otra instancia, en este ejemplo creamos una instancia de 'Vehiculo' 
    llamada 'carrito01' la cual mandamos como argumento para la creación de la
    instancia de 'Empleado' llamada 'empleado01'

        carrito01 = Vehiculo("White", "XYZ 123", es_electrico=False)
        empleado01 = Empleado("Jorge", carrito01)

    Entonces 'carrito01' existira aunque la instancia 'empleado01' no existe

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
    def __init__(self, nombre, vehiculo):
        self.nombre = nombre
        self.vehiculo = vehiculo
        
    def muestra_info_vehiculo(self):
        self.vehiculo.muestra_info()


# podemos especificar el nombre del argumento con el parametro para hacerlo mas
# explicito en este case el argumento es_electrico=False le da mas sentido
carrito01 = Vehiculo("White", "XYZ 123", es_electrico=False)
empleado01 = Empleado("Jorge", carrito01)

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

