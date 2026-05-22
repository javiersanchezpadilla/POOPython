""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Construir nuestro propio with (metodos dunder
    ----------------------------------------------

    with es un protocolo basado en dos métodos especiales (métodos mágicos o 
    dunder methods): __enter__() y __exit__()
    Cualquier clase que implemente estos dos métodos se convierte en un Gestor
    de Contexto.
   
    Para la construcción de nuestros propios Context Managers (Gestores de 
    Contexto), la clave es entender que no son más que clases comunes y 
    corrientes que respetan un 'contrato' o protocolo.
    Este contrato exige que la clase implemente obligatoriamente dos métodos 
    especiales: __enter__() y __exit__()

    Cuando escribimos la estructura:

            with MiContextManager() as variable:
                # Bloque de código (Cuerpo del with)

                
    Python ejecuta lo siguiente de forma secuencial:
    ------------------------------------------------
    1)  Instancia la clase MiContextManager().
    2)  Llama automáticamente al método __enter__(), lo que sea que este 
        método regrese (return), se guarda en la variable designada después 
        del 'as'.
    3)  Se ejecuta todo el código que tenga sangría dentro del with.
    4)  Al terminar ese código (o si ocurre un error/excepción), Python llama 
        de forma obligatoria al método __exit__().

    Ejemplo: cronometro para medir tiempo al ejecutar un código
    aquí creamos los atributos de instancia al vuelo.

    ¿Cómo se conecta return self con el bloque with?
    ------------------------------------------------

    VER EL SIGUIENTE PROGRAMA PARA ENTENDER MEJORA LA EXPLICACIÓN.
"""
import time

class Cronometro:
    def __enter__(self):
        # 1. Al entrar, guardamos el tiempo de inicio
        self.inicio = time.time()
        print("Cronómetro iniciado...")
                    # la palabra clave self representa al objeto mismo que se 
                    # acaba de crear (la instancia de la clase). Cuando un 
                    # método hace return self, lo único que está haciendo es 
                    # decir: "Toma, te devuelvo una copia de mí mismo para que 
                    # la guardes o la uses".
        return self # <<-- Ver el siguiente prog para entender mejor su uso

                    # estos parametros se deben incluir se usen o no
    def __exit__(self, tipo_error, valor_error, traza_error):
        # 2. Al salir, tomamos el tiempo final y calculamos la diferencia
        self.fin = time.time()
        tiempo_total = self.fin - self.inicio
        print(f"Cronómetro detenido. Tiempo transcurrido: {tiempo_total:.4f} segundos.")
        # No manejamos excepciones aquí, devolvemos False de manera implícita


# Uso del Cronómetro
with Cronometro():
    print("Simulando un proceso pesado...")
    time.sleep(1.5)  # Pausa el programa por 1.5 segundos
