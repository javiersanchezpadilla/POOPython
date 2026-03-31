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

    def mostrar_placa_vehiculo(self):
        print(self.placas)

    def mostrar_info_vehiculo(self):
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
        
    def mostrar_info_vehiculo_empleado(self):
        self.vehiculo.mostrar_info_vehiculo()


# podemos especificar el nombre del argumento con el parametro para hacerlo mas
# explicito en este case el argumento es_electrico=False le da mas sentido
carrito01 = Vehiculo("White", "XYZ 123", es_electrico=False)
empleado01 = Empleado("Jorge", carrito01)

# Ejecutamos el método mostrar_info_vehiculo_empleado
empleado01.mostrar_info_vehiculo_empleado()

# Mostramos los atributos de instancia del empleado
print('NOmbre del empleado', empleado01.nombre)
print(empleado01.vehiculo)
# Esto no es posible debido a que no existe dentro de la clase Emplado un 
# atributo llamado carrito01
# print(empleado01.carrito01)

# Accedemos a los atributos de la clase Vehiculo
# esto quiere decir que accedemos a los atributos de instancia
# de la clase vehiculo indirectamente
print('El color del vehiculo es:', empleado01.vehiculo.color)
print('Es electrico', empleado01.vehiculo.es_electrico)
print('Placas:', empleado01.vehiculo.placas)

# Accedemos a los métodos de la clase Vehiculo a traves del
# atributo de clase
empleado01.vehiculo.mostrar_placa_vehiculo()
empleado01.vehiculo.mostrar_info_vehiculo()

# print('Color asignado', empleado01.vehiculo.color)
# print('Las placas son:', empleado01.vehiculo.placas)
# print('Es electrico:', empleado01.vehiculo.es_electrico)


"""
print(empleado01.nombre)
print(empleado01.vehiculo)
# Podemos de forma indirecta llamar a los métodos de la instancia agregada
# sin el intermediario del nombre de la instancia
empleado01.mostrar_info_vehiculo_empleado()

# Llamando metodos de forma indirecta
empleado01.vehiculo.mostrar_placa_vehiculo()

"""