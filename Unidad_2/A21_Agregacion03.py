""" AGREGACIÓN EN LA PROGRAMACIÓN ORIENTADA A OBJETOS.

    Es un concepto en la programación orientada a objetos que describe la 
    relación entre dos o más clases.
    Vamos a construir objetos complejos que se componen de otros objetos, 
    vamos a tomar objetos más simples de clases más simples y vamos a 
    utilizarlos o combinarlos para crear objetos más complejos.
    Digamos que tenemos dos clases, la clase  A y la clase B y necesitamos 
    hacer referencia a la clase A, dentro de la clase B.
    Lo que estamos haciendo aquí es que básicamente estamos utilizando la 
    funcionalidad de la clase A, dentro de la clase B, las clases reales, 
    sus definiciones, aquí todavía no hablamos de instancias ni de objetos, 
    estamos hablando de sus definiciones, estamos creando una especie de 
    relación o conexión entre estas clases.
    La clase B utiliza la funcionalidad o parte de la funcionalidad definida 
    en la clase A, se trata de una relación entre las clases.
    Digamos que creamos instancias de estas clases en nuestra cuenta, instancia 
    de A, una instancia de B cuando creamos esas instancias, dado que B necesita 
    algunas instancias de A para funcionar completamente porque estamos usando 
    la funcionalidad de A dentro de B, necesitaremos proporcionar una instancia 
    de A para crear la instancia de B así.
    La instancia de B de alguna manera almacenará y contendrá la instancia de A 
    dentro de su definición.
    Así podremos acceder a la información y los métodos de la instancia de a 
    dentro de la instancia de B, básicamente estamos almacenando instancias de 
    los objetos más simples en los objetos más complejos.
    Eso es lo que estamos haciendo aquí.
    Digamos que A es un objeto más simple y que B necesita ese objeto, la clase B 
    tiene un objeto de la clase A, así que vamos a almacenarlo dentro de B para 
    poder usarlo.
    Es una relación entre las clases, un objeto de clase B tiene un objeto de clase A,
    estamos usando la funcionalidad de A dentro de B.
"""

class Aula:
    """ La clase 'Aula' representa un salon de clases.
     
    Atributos:
    ----------
    aula        Se indica el número de aula
    descripción Una breve descripción del aula """

    def __init__(self, aula, descripcion_aula):
        self.aula = aula
        self.descripcion_aula = descripcion_aula

    def muestra_aula(self):
        return f'El aula es la número: {self.aula}, {self.descripcion_aula}'


class Materia:
    """La clase 'Materia' permite almacenar una materia con su clave

        Atributos:
        ----------
        clave   clave unica asignada a la materia
        nombre  nombre de la materia"""

    def __init__(self, clave, nombre):
        self.clave = clave
        self.nombre = nombre

    def muestra_materia(self):
        return f'El nombre de la materia es clave: {self.clave} nombre: {self.nombre}'


class Profesor:
    """ La clase profesor se inicializa con un número de tarjeta, un nombre 
        y una instancia de la Materia que imparte
        atributos:
        ----------
        tarjeta             corresponde al número de tarjeta del profesor
        nombre              nombre del profesor
        que_materia_tiene   Instancia de la materia que imparte
        """
    
    def __init__(self, tarjeta, nombre, que_materia_tiene):
        self.tarjea = tarjeta
        self.nombre = nombre
        self.que_materia_tiene = que_materia_tiene

    def muestra_datos_profesor(self):
        return f'El profesor {self.nombre}, imparte la materia {self.que_materia_tiene.clave} {self.que_materia_tiene.nombre}'


class Horarios:
    """ La clase 'Horarios' representa la programación de una materia con una hora 
        inicial, un profesor asignado, así como una aula asignada siendo cada una 
        instancia de las clases 'Profesor' y 'Aula' respectivamente.

        atributos:
        ----------
        hora_inicial        hora inicial de la clase
        que_profesor_tiene  la asignación del profesor
        en_que_aula         asignación del numero de aula """

    def __init__(self, hora_inicial, que_profesor_tiene, en_que_aula):
        self.hora_inicial = hora_inicial
        self.que_profesor_tiene = que_profesor_tiene
        self.en_que_aula = en_que_aula

    def muestra_horario(self):
        print(f'En la hora {self.hora_inicial}')                # Accede a un atributo de la instancia
        print(f'El profesor {self.que_profesor_tiene.nombre}')  # Accede a un atributo de la instancia Profesor
                                                                # Accede a un atributo de la instancia Materia de la instancia
                                                                # de la clase Profesor
        print(f'Imparte la materia de {self.que_profesor_tiene.que_materia_tiene.nombre}')
        print(f'En el aula {self.en_que_aula.aula} {self.en_que_aula.descripcion_aula}')


class Alumnos:
        """ Esta clase de Python define una clase 'Alumno' con atributos para 
            la información de los estudiantes y métodos para mostrar los 
            detalles del horario del estudiante para tres materias diferentes."""


        def __init__(self, matricula, nombre, que_primer_horario_tiene, que_segundo_horario_tiene, que_tercer_horario_tiene):
            self.matricula = matricula
            self.nombre = nombre
            self.hora1 = que_primer_horario_tiene
            self.hora2 = que_segundo_horario_tiene
            self.hora3 = que_tercer_horario_tiene

        def muestra_datos_alumno(self):
            print('===============================================')
            print(f'El alumno {self.matricula} - {self.nombre.upper()}')
            print('MATERIA 1')
            print(f'primer hora {self.hora1.hora_inicial} {self.hora1.que_profesor_tiene.nombre} Aula {self.hora1.en_que_aula.aula} {self.hora1.en_que_aula.descripcion_aula}')
            print(f'materia {self.hora1.que_profesor_tiene.que_materia_tiene.nombre}')
            print('MATERIA 2')
            print(f'primer hora {self.hora2.hora_inicial} {self.hora2.que_profesor_tiene.nombre} Aula {self.hora2.en_que_aula.aula} {self.hora2.en_que_aula.descripcion_aula}')
            print(f'materia {self.hora2.que_profesor_tiene.que_materia_tiene.nombre}')
            print('MATERIA 3')
            print(f'primer hora {self.hora3.hora_inicial} {self.hora3.que_profesor_tiene.nombre} Aula {self.hora3.en_que_aula.aula} {self.hora3.en_que_aula.descripcion_aula}')
            print(f'materia {self.hora3.que_profesor_tiene.que_materia_tiene.nombre}')
            print('===============================================')


# Definicion de las instancias de la clase Aula
aula701 = Aula(701, 'Aula 701')
aula702 = Aula(702, 'Aula 702')
aula703 = Aula(703, 'Aula 703')
print('\nAccedemos a los atributos de la instancia de la clase Aula')
print(aula701.muestra_aula())
print(aula702.muestra_aula())
print(aula703.muestra_aula())

# Definicion de las instancias de la clase Materia
mate_1 = Materia(1, 'Matematicas I')
mate_2 = Materia(1, 'Matematicas II')
fisica = Materia(3, 'Fisica')
print('\nAccedemos a los atributos de la instancia de clase Materia')
print(mate_1.muestra_materia())
print(mate_2.muestra_materia())
print(fisica.muestra_materia())

# Definicion de las instancias de clase Profesor, esta instancia agrega otra 
# instancia de Materia
prof1 = Profesor(100, 'Carlos Arriaga Mendez', mate_1)
prof2 = Profesor(103, 'Maria Candelaria Jimenez', mate_2)
prof3 = Profesor(105, 'Karla Rodriguez Gutierrez', fisica)
print('\nAccedemos a los atributos de la instancia Profesor')
print(prof1.muestra_datos_profesor())
print(prof2.muestra_datos_profesor())
print(prof3.muestra_datos_profesor())

# Muestra la materia del profesor indirectamente
print(prof1.nombre)
print(f'El profesor {prof1.que_materia_tiene.clave}')
print(f'Imparte la materia de {prof1.que_materia_tiene.nombre}\n')
print(prof1.que_materia_tiene.muestra_materia())


print('\n')
hora07_08 = Horarios('07-08', prof1, aula701)
hora08_09 = Horarios('08-09', prof2, aula702)
hora09_10 = Horarios('09-10', prof3, aula703)

hora07_08.muestra_horario()
print(f'El horario {hora07_08.hora_inicial}')
print(f'lo imparte el profesor {hora07_08.que_profesor_tiene.nombre}')
print(f'En el aula {hora07_08.en_que_aula.descripcion_aula}')

# DEfinicion de la instancia de la clase Alumno quien tiene como argumentos, matricula, nombre, instancias 1,2,3 de Horarios
alumno1 = Alumnos('27320001', 'Juan Perez', hora07_08, hora08_09, hora09_10)
alumno2 = Alumnos('29320673', 'Mariana Juarez', hora07_08, hora08_09, hora09_10)
alumno1.muestra_datos_alumno()

# tambien podemos acceder por medio de los atributos
print('*' * 90)
print('Materias para:', alumno1.matricula, alumno1.nombre)
print(alumno1.hora1.hora_inicial, alumno1.hora1.en_que_aula.aula, alumno1.hora1.en_que_aula.descripcion_aula, \
       alumno1.hora1.que_profesor_tiene.que_materia_tiene.nombre, 'Profesor:', alumno1.hora1.que_profesor_tiene.nombre)
print(alumno2.hora1.hora_inicial, alumno2.hora1.en_que_aula.aula, alumno2.hora1.en_que_aula.descripcion_aula, \
      alumno2.hora1.que_profesor_tiene.que_materia_tiene.nombre, 'Profesor:', alumno2.hora1.que_profesor_tiene.nombre)
print('*' * 90)
