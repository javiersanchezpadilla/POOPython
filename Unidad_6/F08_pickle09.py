""" SERIALIZACIÓN CON PICKLE (BINARIO)

    Serializar una Tupla (Datos Inmutables)
    ---------------------------------------
    Las tuplas se utilizan para proteger los datos de modificaciones 
    accidentales (son inmutables). Al recuperar una tupla con pickle, Python 
    garantiza que seguirá siendo inmutable.

    Combinación de Estructuras
    ==========================
    En la práctica, puedes crear colecciones mixtas (por ejemplo: un 
    diccionario donde cada clave es una matrícula y el valor es un objeto de 
    tipo Estudiante). pickle resolverá toda la jerarquía de herencia y 
    referencias internas de forma transparente para el desarrollador.
"""
import pickle
from pathlib import Path

                            # Una tupla que representa las coordenadas 
                            # geográficas de un servidor o campus
coordenadas_campus = (16.8494, -99.8903) 

ruta_tuple = Path.cwd() / "coordenadas.pkl"

                            # Guardar la tupla
with open(ruta_tuple, "wb") as f:
    pickle.dump(coordenadas_campus, f)

                            # Recuperar la tupla
with open(ruta_tuple, "rb") as f:
    tupla_recuperada = pickle.load(f)

print("\nTupla recuperada:")
print(f"Latitud: {tupla_recuperada[0]} | Longitud: {tupla_recuperada[1]}")
