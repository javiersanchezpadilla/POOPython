""" OVERWRITTING (Anulación o reemplazo)

    2. Anulación o Reemplazo Total (Overwriting)
    --------------------------------------------
    Aunque en muchos libros se usa como sinónimo de overriding, en un sentido 
    estricto de Python, el 'overwriting' suele referirse a reemplazar la 
    definición de un método por completo, incluso fuera de la herencia, o 
    simplemente ignorar la lógica del padre sin intención de extenderla.

    Un ejemplo muy claro es cuando 'anulamos' un método asignándole algo 
    distinto (como una variable o una función diferente) en tiempo de 
    ejecución.

    Aquí no hay herencia involucrada en el cambio; hemos 'escrito encima' 
    del método original, anulando su comportamiento inicial por completo.

    Overwriting (Escritura encima): Es más drástico. Es como si cambiaras 
    una pieza del motor por otra que no tiene nada que ver.

    Concepto        ¿Dónde ocurre?      ¿Cómo funciona?     Ejemplo práctico
    --------------------------------------------------------------------------
    Overriding      En la Clase Hija    El hijo tiene su    Un Perro ladra en 
    (sobrescritura)                     propia version      vez de solo 'hacer
                                        del método del      ruido'como el 
                                        padre               animal
                                                            
    Overwriting     En el Objeto        Se reemplaza el     Un Robot que se 
    (Anulación)                         método por algo     rompe y su método 
                                        nuevo               caminar se cambia 
                                        dinámicamente       por una función de 
                                                            error.
"""
class Robot:
    def saludar(self):
        print("Hola, soy un robot.")

def saludo_secreto():
    print("Acceso denegado: Protocolo de seguridad activo.")

# Creamos el objeto
mi_robot = Robot()

# ANULACIÓN (Overwriting): Reemplazamos el método por una función externa
mi_robot.saludar = saludo_secreto

# Prueba
mi_robot.saludar()
