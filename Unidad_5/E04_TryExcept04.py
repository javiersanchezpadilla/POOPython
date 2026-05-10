""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    USO DE EXCEPT SIN ESPECIFICAR TIPO (CAPTURA CUALQUIER EXCEPCIÓN).

    MAlas practicas, jamas hacer esto
   
"""

try:
    resultado = 10 / 0

            # Esto es como tener una alarma de incendio que suena, pero 
            # tú aprietas el botón de silencio y sigues durmiendo. El programa 
            # sigue, pero no sabes que hubo un error y más adelante todo puede 
            # salir peor.

except:
    pass    # Ignorasmosel error completamente (JAMAS HACER ESTO!!!)
