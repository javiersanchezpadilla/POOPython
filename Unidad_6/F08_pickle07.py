""" SERIALIZACIÓN CON PICKLE (BINARIO)

    pickle no tiene ninguna preferencia por las listas; funciona con la misma 
    eficacia con cualquier colección nativa de Python (diccionarios, conjuntos 
    o tuplas). Lo único que hace es analizar la estructura en memoria y 
    transformarla en un mapa de bytes.

    Serializar un Diccionario Complejo
    ----------------------------------
    Los diccionarios son ideales para representar configuraciones de sistemas o 
    registros indexados por una clave única (como una matrícula o un ID).
"""
import pickle
from pathlib import Path

                            # Un diccionario que contiene tipos de datos 
                            # mezclados (strings, enteros y listas)
servidor_config = {
    "ip_host": "192.168.1.100",
    "puerto": 8080,
    "usuarios_permitidos": ["root", "javier", "admin"],
    "modo_estricto": True
}

ruta_dict = Path.cwd() / "config.pkl"

                            # Guardar el diccionario
with open(ruta_dict, "wb") as f:
    pickle.dump(servidor_config, f)

                            # Recuperar el diccionario
with open(ruta_dict, "rb") as f:
    config_recuperada = pickle.load(f)

print("Diccionario recuperado:")
print(f"Conectar a: {config_recuperada['ip_host']}:{config_recuperada['puerto']}")
print(f"Usuarios permitidos: {config_recuperada['usuarios_permitidos']}")
print(f"Modo estricto {config_recuperada['modo_estricto']}")
