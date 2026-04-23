""" OVERRIDING (Extensión de funcionalidad)

    Sobrescritura de Métodos (Overriding)
    -------------------------------------
    Este es el concepto que hemos estado usando. Ocurre cuando una clase hija 
    redefine un método de la clase padre para especializar su comportamiento. 
    El método en el hijo tiene el mismo nombre que el del padre, pero mediante
    esta tecnica extendemos el funcionamiento de un método.

    Overriding (Herencia): Es parte del diseño de clases. Es planeado y 
    estructurado. El hijo dice: 'Yo sé hacer lo mismo que mi padre, pero a mi 
    manera'.

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
class Animal:
    def emitir_sonido(self):
        print("El animal hace un sonido genérico.")

class Perro(Animal):
    # Aquí estamos SOBRESESCRIBIENDO el método del padre
    def emitir_sonido(self):
        print("El perro ladra: ¡Guau, guau!")
        # super().emitir_sonido()

# Prueba
mi_perro = Perro()
# El método del hijo "tapa" al del padre. Si queremos usar ambos, 
# usaríamos super().emitir_sonido().
mi_perro.emitir_sonido()
