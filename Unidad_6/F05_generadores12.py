""" GENERADORES DE TEXTO

    Ejemplo: Lectura Eficiente de un Archivo de Texto MUY GRANDE
    ------------------------------------------------------------
    Este es un caso de uso real en la ingeniería de datos. Imagina que en tus 
    servidores Linux tienes un archivo de bitácora (log) que mide 10 Gigabytes
    Si intentas hacer un open().readlines(), tu servidor se quedará sin 
    memoria RAM y el sistema operativo colapsará el programa.

    Al combinar open() con yield, puedes leer el archivo línea por línea de 
    forma ultra eficiente:

"""
from pathlib import Path

def leer_bitacora_por_linea(ruta_archivo):
                            # Usamos el gestor de contexto dentro del 
                            # generador
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
                            # Quitamos espacios en blanco o saltos de línea al 
                            # final
            linea_limpia = linea.strip()
            
                            # Solo enviamos la línea si contiene una palabra 
                            # clave de error
            if "ERROR" in linea_limpia:
                yield linea_limpia 


                            # Simulamos el procesamiento
ruta_log = Path.cwd() / "servidor.log"
                            # Creamos un archivo de prueba rápido
ruta_log.write_text("INFO: Servidor iniciado\nERROR: Conexión fallida en BD\nINFO: Reintentando\nERROR: Timeout")

                            # Consumimos el generador
for linea_error in leer_bitacora_por_linea(ruta_log):
    print(f"Alerta detectada: {linea_error}")
