""" MÉTODOS ESTÁTICOS EN PYTHON

    Dentro de una clase podemos tener dos tipos de métodos, por un lado 
    métodos estáticos y también vamos a tener métodos de clase específicamente.

    Métodos Estáticos. se asocian con la clase directamente y no con los 
    objetos, para declararlos debemos hacer uso de un decorador  @staticmethod 
    un método estático no puede acceder a las variables de instancia y estas 
    se crean solamente al momento de crear el objeto y al momento de la 
    creación de la clase aún no se han creado objetos, lo cual ya pueden 
    asignarse hasta el momento en que se encuentre cargada en memoria.

    Cuando trabajamos con nuestra clase (en la creación) estamos trabajando en 
    un contexto estático y cuando ya creamos los objetos se dice que estamos 
    trabajando en un contexto dinámico. un método estático además no puede 
    acceder a las variables de instancia porque además no recibe el argumento 
    self. (def metodo_estatico(  ):) así que no podrá acceder desde un método 
    estático a ningún atributo.
"""

class MiClase:
    variable_clase = 'Valor variable'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

MiClase.metodo_estatico()
