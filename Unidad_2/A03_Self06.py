""" Este ejemplo mostrará un error en la creación de un objeto

    En este ejemplo pronaremos porque es necesario el uso de self o el nombre
    que deseemos

    Este error es desconcertante para los alumnos cuando empiezan con POO. 
    Vamos a crear el "Ejemplo Trampa" que puedes mostrarles en pantalla para 
    explicarles por qué el primer parámetro (aunque no se llame self) es vital.

    La Trampa: El parámetro "invisible"
    Presenta este código a tus alumnos y pídeles que adivinen por qué falla:
    
    El error obtenido es 
        Traceback (most recent call last):
        File "/home/javier/Documentos/Progs.../A03_Self06.py", line 19, in <module>
        n1 = Nave(10, 20)
            ^^^^^^^^^^^^
        TypeError: Nave.__init__() takes 2 positional arguments but 3 were given
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    Esto se debe a que cuando creamos un objeto o instancia, por ejemplo

        n1 = Nave(10, 20)
    
    Realmente lo que se está ejecutando internamente es:

        Nave.__init__(n1, 10, 20)   Como vemos llama al método __init__ con 3 
                                    argumentos

    El objeto 'n1' se "inyecta" automáticamente en el primer lugar de la lista de 
    parámetros. 
    El nombre que le pongas a ese receptor en la definición de la clase es el que 
    usarás para acceder a los datos.

    ¿Por qué dice que recibió 3 argumentos si solo pasamos 10 y 20?

    Aquí es donde ocurre la "magia" (y la confusión). Para explicarlo, usa esta analogía:
    Cuando tú haces n1 = Nave(10, 20), Python hace un trabajo de mensajería automática 
    por detrás:

        1) Crea el objeto en memoria.
        2) Llama al constructor enviando 3 cosas:
            2.1) La Identidad del objeto (el propio n1).
            2.2) El valor 10.
            2.3) El valor 20.


    Como en la definición de def __init__(x, y): solo preparaste dos sillas (parámetros), 
    cuando Python llega con tres invitados (n1, 10 y 20), el programa "explota" porque no 
    sabe dónde sentar al primer invitado (n1).

    La solución (con cualquier nombre)
    Para que funcione, siempre debemos dejar una silla especial en primer lugar para el objeto:

            class Nave:
                # 'yo' ocupará el lugar del objeto n1
                def __init__(yo, x, y): 
                    yo.x = x
                    yo.y = y

            n1 = Nave(10, 20) # Ahora sí: 3 invitados para 3 sillas.

    Puntos clave para la clase:
     1) El primer parámetro es el receptor: No importa cómo se llame, su trabajo es recibir al 
        objeto que Python envía automáticamente.
     2) La confusión del nombre: Si llamas al primer parámetro 'x', entonces dentro del método 'x' 
        sería el objeto, ¡y eso sería un caos total! Por eso usamos self.
     3) Visualización de la memoria:
            3.1) n1.x guarda el dato en la memoria del objeto.
            3.2) x (sin el punto) es solo una variable temporal que muere cuando termina el método.
    """

class Nave:
    
    def __init__(x, y):         # Error común: olvidar el parámetro para la instancia
        x = x
        y = y

# Intentamos crear la instancia de 'Nave'
n1 = Nave(10, 20)
