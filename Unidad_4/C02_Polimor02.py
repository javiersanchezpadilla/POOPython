""" POLIMORFISMO.

    3. Duck Typing: El Polimorfismo en Python
    -----------------------------------------
    Python es un lenguaje de tipado dinámico, lo que permite un polimorfismo 
    mucho más flexible llamado Duck Typing (Tipado de Pato).

    'Si camina como un pato y grazna como un pato, entonces es un pato'.

    En Python, no necesitas que las clases hereden del mismo padre para que 
    haya polimorfismo. Solo necesitan tener el método con el mismo nombre.

"""
class Radio:
    def encender(self):
        print("Sintonizando frecuencia...")

class Lampara:
    def encender(self):
        print("Iluminando la habitación...")

# Esta función no pregunta "¿De qué clase eres?", 
# solo pregunta "¿Tienes el método encender()?"
def activar_dispositivo(objeto):
    objeto.encender()

activar_dispositivo(Radio())
activar_dispositivo(Lampara())
