""" PATRONES DE DISEÑO (CREACIONALES)

    Entrar al mundo de los Patrones de Diseño es pasar de ser un programador 
    que escribe código funcional a ser un Arquitecto de Software, esto es 
    fundamental porque los patrones son soluciones probadas a problemas 
    comunes en el desarrollo de software.

    1. Definición de Patrones de Diseño
    -----------------------------------
    Un patrón de diseño es una solución estándar y reutilizable a un problema 
    que ocurre frecuentemente en un contexto de diseño de software.
    No es una pieza de código terminada que se copia y pega, sino una 
    plantilla o guía sobre cómo resolver un problema. Es el 'lenguaje común' 
    entre ingenieros; cuando dices 'usa un Singleton', todos entienden la 
    arquitectura sin ver una sola línea de código.

    2. Tipos de Patrones de Diseño
    ------------------------------
    Se dividen en tres grandes familias según el tipo de problema que 
    resuelven:

    1)  Creacionales: Se enfocan en cómo se crean los objetos. Su objetivo es 
        separar la lógica de creación de la lógica de uso para que el sistema 
        sea independiente de cómo se crean sus objetos.
    2)  Estructurales: Se enfocan en cómo se combinan las clases y objetos 
        para formar estructuras más grandes y eficientes (como piezas de LEGO 
        que encajan perfectamente).
    3)  De Comportamiento: Se enfocan en la comunicación entre objetos. 
        Definen cómo los objetos interactúan y se reparten las 
        responsabilidades.

        

    3. PATRONES CREACIONALES: EJEMPLO - SINGLETON
    =============================================
    El patrón Singleton garantiza que una clase tenga una única instancia en 
    todo el programa y proporciona un punto de acceso global a ella.

    Ejemplo práctico: Una conexión a una base de datos o un gestor de 
    configuración. No quieres 100 conexiones abiertas, quieres una sola 
    compartida por todos.

    1. La Analogía: 'El interruptor de la luz'
    ------------------------------------------
    Imagina que en un salón de clases hay un solo interruptor. No importa 
    cuántos alumnos entren al salón e intenten 'instalar un nuevo interruptor'
    el salón ya tiene uno. Si un alumno intenta poner otro, el salón 
    simplemente le entrega el que ya existe. Al final, todos los alumnos están 
    tocando el mismo objeto.

    Eplicación del código
    El secreto del Singleton está en controlar el momento exacto en que el 
    objeto nace.

    A) La variable de clase _instancia

            _instancia = None

    Esta es una variable 'estática' o de clase. Sirve como nuestra memoria. 
    Al inicio es None porque aún no hemos creado nada. Aquí guardaremos el 
    interruptor una vez que se fabrique.

    B) El método mágico __new__

            def __new__(cls):

    A diferencia de __init__ (que inicializa un objeto que ya existe), __new__ 
    es el encargado de crear el objeto físicamente en la memoria.

    cls representa a la clase misma (ConfiguracionSistema).

    C) La 'Puerta de Seguridad' (El if)

            if cls._instancia is None:
                cls._instancia = super(ConfiguracionSistema, cls).__new__(cls)

    Aquí sucede la magia:
    **) Primera vez: Cuando haces config1 = ConfiguracionSistema(), Python 
        pregunta: ¿_instancia es None?. Como es verdad, usa 
        super().__new__  para crear el objeto por primera vez y lo guarda en 
        _instancia.
    **) Segunda vez: Cuando haces config2 = ConfiguracionSistema(), Python 
        vuelve a preguntar: ¿_instancia es None?, Ahora es Falso Porque ya 
        tiene guardado el objeto anterior.
    **) Resultado: Se salta la creación y simplemente te devuelve lo que ya 
        tenía guardado.

    3. ¿Por qué esto es un patrón "Creacional"?
    -------------------------------------------
    Se llama así porque el patrón toma el control de la creación.
    En una clase normal, cada vez que usas paréntesis (), creas un objeto 
    nuevo en una dirección de memoria distinta. En el Singleton, el patrón 
    'secuestra' ese proceso de creación para asegurar que, sin importar 
    cuántas veces pidas un objeto, siempre recibas el mismo.

    Ejemplo práctico de por qué lo usamos:
    Si estamos programando un juego, la clase Configuracion (volumen, 
    resolución, brillo) debe ser un Singleton. Si el Jugador cambia el volumen 
    a 50%, la Musica debe ver ese mismo 50%. Si fueran objetos distintos, el 
    jugador cambiaría el volumen en un objeto y la música seguiría leyendo el 
    valor del otro objeto.

    Por esta razon config1 is config2 da True (No es que sean parecidos), es 
    que son literalmente el mismo espacio de memoria con dos nombres 
    diferentes.
"""
class ConfiguracionSistema:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando instancia única de configuración...")
            cls._instancia = super(ConfiguracionSistema, cls).__new__(cls)
        return cls._instancia

# Prueba
config1 = ConfiguracionSistema()
config2 = ConfiguracionSistema()

print(f"¿Son la misma instancia? {config1 is config2}") # True
