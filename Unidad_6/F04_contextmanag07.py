""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Ejemplo: Formateador de Reportes (Etiquetas HTML/Texto)
    asegura que si abrimos una sección de diseño o un formato decorativo en 
    consola, este se cierre correctamente al terminar, evitando dejar la 
    pantalla distorsionada.
"""
class DiseñadorBloque:
    def __init__(self, titulo):
        self.titulo = titulo

    def __enter__(self):
        print(f"\n=================== {self.titulo} ===================")
        return None  # No necesitamos asignar nada a una variable con 'as'

    def __exit__(self, tipo, valor, traza):
        # Al salir, cerramos el bloque visual de manera simétrica
        print("===================================================\n")

# Uso del Diseñador
with DiseñadorBloque("DATOS DEL ALUMNO"):
    print("Nombre: Javier")
    print("Matrícula: 20120987")
