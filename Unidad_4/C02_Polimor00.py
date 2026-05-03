""" POLIMORFISMO.

    En Polimorfismo, no basta con saber que 'os objetos cambian de forma'. 
    Se debe entender cómo esta capacidad permite construir sistemas 
    desacoplados (donde las piezas no dependen rígidamente unas de otras).
    Aspectos fundamentales a cubrir:

    1. El Concepto de Interfaz Común
    --------------------------------
    Es el aspecto más básico pero vital. Se  debe entender que el 
    polimorfismo requiere que DIFERENTES CLASES COMPARTAN EL MISMO NOMBRE DE 
    MÉTODO y los mismos parámetros, aunque el código interno sea distinto.
    La analogía: El botón 'Encender' de un microondas, una PC y un auto. La 
    acción es la misma, el proceso interno es radicalmente diferente.
    
    2. Sobrescritura de Métodos (Method Overriding u overwritting)
    ------------------------------------------------
    Es la base técnica. Para aprender polimorfismo, deben dominar cómo una 
    subclase redefine el comportamiento de la superclase.
    Punto clave: Entender cuándo usar super() para complementar al padre y 
    cuándo reemplazarlo por completo.
    
    3. Duck Typing (Tipado de Pato) en Python
    -----------------------------------------
    Este es un aspecto específico de Python que lo diferencia de lenguajes 
    como Java o C++. Lo que deben aprender: Python no verifica el tipo de 
    objeto (la clase), sino la presencia del método.
    'Si camina como pato y grazna como pato, es un pato'. Esto permite 
    polimorfismo entre clases que no tienen ninguna relación de herencia 
    entre sí.
    
    4. Clases Abstractas y Métodos Abstractos (ABC)
    -----------------------------------------------
    En ingeniería, esto es fundamental para el diseño de contratos.
    El concepto: Una clase 'padre' que obliga a todos sus hijos a implementar 
    ciertos métodos.
    Herramienta: El módulo abc de Python. Si un hijo no implementa el método 
    atacar(), Python no permitirá crear el objeto. Esto garantiza que el 
    polimorfismo no falle en tiempo de ejecución.
    
    5. Colecciones Heterogéneas
    ---------------------------
    Es la aplicación práctica más potente. Los alumnos deben aprender a 
    guardar objetos de distintas clases en una sola lista y procesarlos con un 
    ciclo simple.
    Ejemplo: Una lista [Bala(), Jugador(), Pared()] donde a todos se les llama 
    el método renderizar().
    
    Orden de dificultad:
    
    Nivel           Tema                        Objetivo Práctico
    Básico      Overriding              Cambiar el comportamiento de un método
                                        heredado.
    Intermedio  Listas Polimórficas     Recorrer una lista de diferentes 
                                        objetos y ejecutar un método común.
    Avanzado    Duck Typing             Lograr que dos clases sin parentesco 
                                        funcionen en la misma función.
    Ingeniería  Abstract Base Classes   Crear una 'plantilla' obligatoria para 
                                        nuevos desarrolladores.
                                        
    'La Herencia es para reutilizar código; el Polimorfismo es para desacoplar 
    código'.
    
    Si el código del motor del juego no sabe si está moviendo un dragón o una 
    nave, entonces el programador puede añadir 100 tipos de enemigos nuevos sin 
    tocar ni una sola línea del motor. Eso es eficiencia ingenieril.


"""