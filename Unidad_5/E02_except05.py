""" MANEJO DE EXCEPCIONES USANDO CLASES

    Sistema de Gestión de Archivos de Configuración
    -----------------------------------------------
    En este ejemplo, una clase intenta leer una configuración y luego 
    aplicarla. Son dos procesos distintos que requieren su propio manejo.
"""
class GestorConfiguracion:
    def __init__(self, ruta):
        self.ruta = ruta
        self.datos = None

    def ejecutar(self):                 # Lectura del archivo
        try:
            with open(self.ruta, "r") as f:
                # Cuando hacemos self.datos = f.read(), lo que el programa 
                # obtiene es una cadena de texto (un string) con todo lo que 
                # hay dentro del archivo.
                self.datos = f.read()

            print("Archivo leído con éxito.")
        except FileNotFoundError:
            print("Archivo no encontrado. Usando configuración por defecto.")
            self.datos = "default_mode=on"

        try:                            # Procesamiento de los datos
            # La expresión if "error" in self.datos: es una forma muy común 
            # (en python) de buscar una subcadena dentro de otra. El programa 
            # simplemente escanea el texto buscando la palabra literal "error".
            # ¿De dónde saldría ese "error"?
            # En un escenario real, esto se usa por dos razones:
            # Archivos Corruptos: A veces, ciertos sistemas operativos o 
            # sensores escriben la palabra "error" dentro del archivo cuando 
            # fallan al guardar los datos.
            # Marcadores de Seguridad: Como programador, tú podrías decidir 
            # que si el archivo de configuración contiene la palabra "error" 
            # (quizás porque alguien lo editó mal), el sistema no debe 
            # arrancar por seguridad.

            # En caso (pero solo en caso) de que les cause conflicto en lugar
            # de buscar "error", validamos que no esté vacío
            # if len(self.datos) == 0:
            #     raise ValueError("Archivo vacío, no hay nada que config.")

            if "error" in self.datos:
                raise ValueError("Contenido corrupto")

            print(f"Configuración aplicada: {self.datos}")
            
        except ValueError as e:
            print(f"No se pudo aplicar la configuración: {e}")


app = GestorConfiguracion("config.txt")
app.ejecutar()
