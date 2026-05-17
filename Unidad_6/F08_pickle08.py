""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Serializar un Conjunto o Set (Datos Únicos)
    -------------------------------------------
    Los conjuntos (set) se usan cuando necesitas asegurar que no existan 
    elementos duplicados (por ejemplo, una lista de asistencias o claves 
    únicas registradas en el día). pickle mantiene las propiedades del 
    conjunto intactas al recuperarlo.
"""
import pickle
from pathlib import Path

                            # Un conjunto con elementos únicos (los 
                            # duplicados se eliminan automáticamente)
asistencia_laboratorio = {"20120001", "20120002", "20120003", "20120001"} 

ruta_set = Path.cwd() / "asistencia.pkl"

                            # Guardar el conjunto
with open(ruta_set, "wb") as f:
    pickle.dump(asistencia_laboratorio, f)

                            # Recuperar el conjunto
with open(ruta_set, "rb") as f:
    set_recuperado = pickle.load(f)

print("\nConjunto (Set) recuperado:")
print(set_recuperado)
print(f"¿La matrícula 20120001 asistió?: {'Sí' if '20120001' in set_recuperado else 'No'}")
