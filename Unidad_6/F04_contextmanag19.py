""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Construir nuestro propio with (metodos dunder
    ----------------------------------------------

    with es un protocolo basado en dos métodos especiales (métodos mágicos o 
    dunder methods): __enter__() y __exit__()
    Cualquier clase que implemente estos dos métodos se convierte en un Gestor 
    de Contexto.
    Imaginemos que diseñamos el software para un laboratorio de cómputo donde 
    los alumnos deben firmar su entrada y salida de un servidor de forma 
    obligatoria:

    Resultado:
        Conectando al servidor en 192.168.1.50...
        Sesión iniciada y recursos asignados.
        El alumno está ejecutando consultas en la Base de Datos...
        Limpiando búfer de memoria...
        Conexión con 192.168.1.50 cerrada de forma segura.
        --- Fin del script ---
"""
class ConexionServidor:
    def __init__(self, ip):
        self.ip = ip

    def __enter__(self):
        """Define qué pasa al iniciar el bloque 'with'"""
        print(f"Conectando al servidor en {self.ip}...")
        print("Sesión iniciada y recursos asignados.")
        return self # Este objeto es el que se asigna a la variable después del 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Define qué pasa al salir del bloque, pase lo que pase
        
            args: (deben colocarse siempre se usen o no)
            exc_type: tipo de excepcion
            exc_val: numero de excepción
            exc_tb: trazabilidad del error
            """
        print("Limpiando búfer de memoria...")
        print(f"Conexión con {self.ip} cerrada de forma segura.")
        
        # Si regresamos True, mitigamos cualquier excepción interna. 
        # Si regresamos False o None, dejamos que la excepción continúe su flujo.
        return False 

# Uso del Gestor de Contexto Personalizado
with ConexionServidor("192.168.1.50") as servidor:
    print("El alumno está ejecutando consultas en la Base de Datos...")
    # Incluso si aquí ponemos un 'return' o un 'raise', el servidor se cerrará.

print("****************** Fin del script")
