""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

       Ejemplo: cronometro para medir tiempo al ejecutar un código
    aquí creamos los atributos de instancia al vuelo.

    ¿Cómo se conecta return self con el bloque with?
    ------------------------------------------------

    Cuando construimos un Gestor de Contexto y usamos la palabra clave 'as', 
    Python hace una asignación automática de variables.

            with Cronometro() as mi_reloj:
                # Código adentro...

    Python ejecuta el método __enter__(), lo que sea que regrese (return) el 
    método __enter__() es lo que se va a guardar dentro de la variable 
    mi_reloj.
    Si en __enter__() regresas self, la variable mi_reloj se convierta en el 
    objeto Cronometro que se está ejecutando.

    Un ejemplo práctico para ver la utilidad
    ----------------------------------------
    ¿Para qué querríamos tener el objeto guardado en la variable del 'as'? 
    Para poder interactuar con él mientras el bloque está activo.

    Modifiquemos ligeramente el ejemplo del cronómetro para entender cómo 
    podemos usar la variable mi_reloj gracias al return self:

    ¿Qué pasa si NO pones return self?
    -----------------------------------
    Si no escribimos el return en el método __enter__() (o return None), el 
    código seguirá funcionando perfectamente siempre y cuando no uses la 
    palabra clave 'as'.

    Si intentas hacer with Cronometro() as mi_reloj: sin haber puesto el 
    return self, la variable mi_reloj recibirá el valor de None, y si intentas 
    interactuar con ella después, Python arrojará un error (AttributeError: 
    'NoneType' object has no use...).

    return self es el puente que le permite a Python pasarle las propiedades y 
    métodos del Gestor de Contexto a la variable que pones después del 'as'. 
    Esto se conoce como un patrón de diseño de interfaz fluida o 
    encadenamiento.
"""
import time

class Cronometro:
    def __enter__(self):
        self.inicio = time.time()
        print("Cronómetro iniciado...")
        # Al regresar self, permitimos que el 'as' capture este objeto completo
        return self  

    def tiempo_parcial(self):
        """Método extra para consultar el tiempo sin detener el cronómetro."""
        actual = time.time()
        return actual - self.inicio

    def __exit__(self, tipo, valor, traza):
        self.fin = time.time()
        print(f"Fin del bloque. Total: {self.fin - self.inicio:.4f} seg.")


                                    # PROBAMOS EL CÓDIGO
with Cronometro() as mi_reloj:
    # mi_reloj AHORA MISMO TIENE EL OBJETO CRONÓMETRO ADENTRO
    
    time.sleep(0.5)
    # Podemos llamar a métodos del objeto en tiempo real
    print(f"   [Vuelta 1] Tiempo parcial: {mi_reloj.tiempo_parcial():.4f} seg.")
    
    time.sleep(0.5)
    print(f"   [Vuelta 2] Tiempo parcial: {mi_reloj.tiempo_parcial():.4f} seg.")
