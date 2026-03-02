""" Properties

    Ya sabemos cómo trabajar con getters y setters, vamos a empezar a
    bucear en las propiedades en python getters y setters son muy 
    comúnmente utilizados en la programación orientada a objetos, ya 
    que nos ayudan a seguir e implementar el principio de encapsulación,
    mostrando sólo los atributos que queremos mostrar al mundo exterior.
    Pero en Python, normalmente no trabajamos con getters y setters, al 
    menos no directamente, porque tenemos una alternativa mejor.

    Pensemos que tenemos una clase, que resuelve poder ver y cambiar
    el atributo de la edad (todo de forma normal)
    class Perro:
        def __init(self, edad):
            self.edad = edad                            <-- 
            
    perro1 = Perro(5)
    print(f'La edad de mi perro es {perro1.edad}')      <--
    print('Dentro de un año tendra...')
    perro1.edad += 1                                    <--
    print(f'Mi perro tiene ahora {perro1.edad}')        <--

    El problema ocurre si queremos ahora cambiar el atributo 'edad' como no
    público '_edad', en todo el código accedimos como perro1.edad en lugar de 
    perro1._edad (uso del guión bajo), en ese momento si ejcutamos el código
    obtendremos errores porque ahora el atributo de instancia se llama 
    'perro1._edad' y todos los accesos fueron sin el guion bajo ('perro1.edad)

    class Perro:
        def __init(self, edad):
            self._edad = edad       <-- Aqui cambiamos a no publico de edad a _edad

    perro1 = Perro(5)
    print(f'La edad de mi perro es {perro1.edad}')  <--  Error debe ser perro1._edad
    print('Dentro de un año tendra...')
    perro1.edad += 1                                <--  Error debe ser perro1._edad
    print(f'Mi perro tiene ahora {perro1.edad}')    <--  Error debe ser perro1._edad

    Para resolver esto, no es necesario volver a reescribir el código ya que en ete 
    ejemplo son solo tres lineas, pero pensemos que son muchas y muchas lineas, para
    resolver esto, usamos una propiedad asignada a aun atributo de instancia, 
    practicamente lo que vamos a hacer es crear una como etiqueta para que '_edad' 
    sea reconocida como 'edad' y así no tener que reescribir el programa cambiando 
    cada uno de los accesos de 'perro1.edad' por 'perro1._edad', lo primero que haremos
    será crear los getters y setters para acceder al atributo de instancia '_edad' y 
    posteriormente createmos la propiedad hacia 'edad'

            property(<getter>, <setter>)  
            <property_name> = property(<getter>, <setter>)  

    De acuerdo a nuestra clase el atributo es self._edad, pero las referencias en el
    código lo hacen a <perro1.edad>, entonces para no tener que cambiar todo a 
    <perro1._edad>, simplemente creamos una propiedad donde '_edad' lo asignamos a 'edad'

    edad = property(get_edad, set_edad)

    DE esta forma cuando el usuario quiera mostrar el valor print(perro1.edad), realmente
    estará llamando al método get_edad(self), de igual manera cuando el usuario quiera 
    cambiar un valor perro1.edad = 3, realmente estará llamando al set_edad(self, new_edad)
    Para comprobarlo podemos colocar un print('Llamando al SETTER') o 
    print('Llamando al GETTER') dentro de la función para entender mejor su funcionamiento
"""
class Perro:
        
        def __init__(self, edad):
            self._edad = edad           # la asignacion original era self.edad

        def get_edad(self):             # Creamos el getter sobre _edad
              return self._edad
    
        def set_edad(self, new_edad):   # Creamos el setter sobre _edad
              if isinstance(new_edad, int) and 0 < new_edad < 30:
                    self._edad = new_edad

        edad = property(get_edad, set_edad)

perro1 = Perro(5)
print(f'La edad de mi perro es {perro1.edad}')
print('Dentro de un año tendra...')
perro1.edad += 1
print(f'Mi perro tiene ahora {perro1.edad}')
