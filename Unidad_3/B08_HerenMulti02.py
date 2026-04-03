"""
    HERENCIA MÚLTIPLE EN PYTHON

    Ya sabemos más sobre la herencia multinivel, ahora hablemos de la 
    herencia múltiple.
    En herencia múltiple, una clase tiene más de una clase principal.

    Por ejemplo, si estamos desarrollando una interfaz gráfica de usuario 
    (GUI), una clase de botón podría heredar tanto de la clase Rectángulo 
    (para estilo) como de la clase GUIEelement (para funcionalidad).

    Este es un diagrama de esta jerarquía:

    Rectangulo  
              \
               \
                +------> Boton
               /
              /
    GUIElement

    Esta es la sintaxis general para configurar la herencia múltiple. 
    La subclase heredará los atributos y métodos de ambas superclases 
    (clases base).

    Hay que tener en cuenta que la herencia múltiple es muy diferente de la 
    herencia multinivel, incluso si sus nombres pueden parecer similares. 
    Tómese un momento para analizar sus diferencias.
"""

class Rectangulo:
 
    def __init__(self, longitud, ancho, color):
        self.longitud = longitud
        self.ancho = ancho
        self.color = color
 
 
class GUIElement:
 
    def click(self):
        print("El objeto ha sido oprimido con un clic...")
 
 
class Boton(Rectangulo, GUIElement):
 
    def __init__(self, longitud, ancho, color, texto):
        Rectangulo.__init__(self, longitud, ancho, color)
        self.texto = texto

