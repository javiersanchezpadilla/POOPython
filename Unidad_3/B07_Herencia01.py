""" HERENCIA

    Consiste en definir clases que heredan atributos y métodos de otras clases
    como un arbol

    Ventajas:
    ---------
    A) reduce repetir código
    B) Reusamos código
    C) Mejora la legibilidad del código

    Ejemplo:
    --------
    Suponer que queremos representar un triangulo y un cuadrado. podemos
    observar que ambos tienen:
    1) un determinado numero de lados 
    2) un color

    Asi mismo pueden tener funcionalidades similares como 
    1) mostrar los lados
    2) mostrar el color
    3) cambiar el color

    En una palabra ambas figuras pueden hererar estas caracteristicas de una 
    clase superior llamada poligono, de esta manera si es necesario crear una
    nueva clase llamada rectangunlo no existiria ningun problema en hacer
    que la nueva clase herede tambien de la clase poligono y toda la 
    funcionalidad que necesitaremos que es compartida por todos estos 
    poligonos y que ya estará definida en la clase poligono.
    Las clases suelen heredar de clases mas generales que representan 
    conceptos mas abstractos. Por ejemplo es mas dificil imagenar un poligono
    que un triangulo, un rectangulo o un cuadrado, sin embargo definimos la
    funcionalidad general en la clase padre ne nuestro atributos y métodos y 
    posteriormete agergamos nuevas funcionalidades a las clases hijas,así que
    estamos reutilizando código de la clase padre y extendiendolo o 
    personalizandolo en la clase hija.

    Otro ejemplo puede ser un carro y un camion, donde ambos son vehiculos, 
    ambos tienen atributos y funcionalidades comunes como encender el motor,
    mostrar el combustible restante, acelerar, así que podemos crear una clase
    mas general llamada vehiculo para escribir el código compartido de esa
    clase mas general.

    REGLA PARA IDENTIFICAR UNA CLASE HIJA Y UNA CLASE PADRE 
    -------------------------------------------------------

    clase hija ES UN(A) clase padre

    Ejm.
    carro ES UN un vehiculo     carro hereda de vehiculo
    camion ES UN vechiculo      caminon hereda de vehiculo
    cuadro ES UN poligono       cuadro hereda de poligono
    triangulo ES UN poligono    triangulo hereda de poligono
    pastel ES UN postre         pastel hereda de postre
    helado ES UN postre         helado hereda de postre
    perro ES UN animal          perro hereda de animal
    gato ES UN animal           gato hereda de animal

    UNA CLASE TAMBIEN PUEDE HEREDAR DE MULTIPLES CLASES Y MULTIPLES CLASES
    TAMBIEN PUEDEN HEREDAR DE LA MISMA CLASE

    Vehiculo ---> VehiculoTerestre ----> Carro
                                   ----> Camion

    Terminología y consejos importantes
    -----------------------------------
    Clase padre (superclase)
    **) La clase de la que otras clases heredan atributos y métodos (por 
        ejemplo, Vehiculo).
    **) Clase hija (Subclase)
        La clase que hereda atributos y métodos de otra clase (por ejemplo, 
        Carry y Camion).

    La clase hija (subclase) hereda de la clase padre (superclase). 
    Tenga en cuenta que en Python, cada clase se deriva de la clase OBJECT.

        class SuperClase:
            pass
            
        class Subclase(Superclase)
            pass

    Herencia en contexto: evitar la repetición de código
    ----------------------------------------------------

    Revisar las siguientes dos clases. ¿No notas algo un poco extraño?
    Hay mucho código repetido.
    Ambas clases tienen los atributos nombre, edad, dirección, teléfono, 
    salario y bonificación_mensual.
    salario y bonificación_mensual incluso tienen el mismo valor.
    DRY (Dont Repeat Yourself) es un principio clave del desarrollo de 
    software, por lo que debe haber una manera de solucionarlo, ¿verdad?

    La herencia es la clave para evitar toda esta repetición.
"""
class Programmer(object):
    
    salario = 100000
    bonificacion_mensual = 500
    
    def __init__(self, nombre, edad, direccion, telefono, lenguajes_programacion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.lenguajes_programacion= lenguajes_programacion
 
class Engineer(object):
    
    salario = 100000
    bonificacion_mensual = 500
    
    def __init__(self, nombre, edad, direccion, telefono, bilingue):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.bilingue = bilingue

