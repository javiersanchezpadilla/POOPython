""" ¿el nombre 'self' es obligatorio?
    ¿puede usarse otro nombre? ¿no precisamente 'self'?
    
    Técnicamente NO es obligatorio, pero socialmente es IMPRESCINDIBLE.
    Diferencia entre lo que el lenguaje permite y lo que los programadores aceptan.

    1. La regla técnica (Lo que Python permite)
    -------------------------------------------
    Para Python, self no es una palabra reservada (como lo son if, while o class). 
    Es simplemente el primer parámetro de un método de instancia. Python solo 
    exige que el primer argumento de estos métodos reciba la referencia al objeto, 
    pero no le importa cómo lo llames.

    En este ejemplo, cambiamos self por mipropia_nave y el programa corre sin 
    errores.        

                class Nave:
                def __init__(mipropia_nave, x, y):
                    # Usamos 'mipropia_nave' en lugar de 'self'
                    mipropia_nave.x = x
                    mipropia_nave.y = y

                n1 = Nave(10, 20)
                print(n1.x)  # Imprime 10

    2. La regla social (Por qué DEBES usar self)
    --------------------------------------------
    Aunque Python te deje usar otros nombres, hay razones muy poderosas 
    para no hacerlo:
    A)  Legibilidad Universal: Todos los programadores de Python del mundo esperan 
        ver self. Si usas otro nombre, tu código será mucho más difícil de leer para 
        otros (o para ti mismo en el futuro).
    B)  Guía de Estilo (PEP 8): El documento oficial de estilo de Python (PEP 8) establece 
        explícitamente que se debe usar self para los métodos de instancia.
    C)  Ayuda del Editor: Muchos editores de código (como VS Code o PyCharm) colorean self 
        de forma especial o te ayudan a completar el código. Si usas otro nombre, pierdes 
        estas ayudas.

    3. ¿Cómo funciona "mágicamente" el primer parámetro?
    ----------------------------------------------------
    Lo que realmente importa es que, cuando llamas a un método (como el constructor), 
    Python hace un envío automático:

    1)  Tú escribes: n1 = Nave(10, 20)
    2)  Python lo traduce internamente a: Nave.__init__(n1, 10, 20)

    El objeto n1 se "inyecta" automáticamente en el primer lugar de la lista de parámetros. 
    El nombre que le pongas a ese receptor en la definición de la clase es el que usarás 
    para acceder a los datos.

    Resumen para los alumnos:
    Si un alumno te pregunta esto, una buena analogía es el idioma:
    "Tú puedes decidir llamar 'perro' a un gato. Si tú lo entiendes, está bien. Pero cuando 
    intentes hablar con otras personas, nadie sabrá de qué estás hablando. En Python, self 
    es el idioma universal de los objetos."                
""" 

class Nave:
    def __init__(mipropia_nave, x, y):
        # Usamos 'mipropia_nave' en lugar de 'self'
        mipropia_nave.x = x
        mipropia_nave.y = y

n1 = Nave(10, 20)
print(n1.x)  # Imprime 10
