""" GENERADORES DE TEXTO

    Nivel Avanzado: Generación Infinita de Cadenas (Tokens o Folios)
    ----------------------------------------------------------------

    Como los generadores no almacenan los resultados pasados en la memoria, 
    puedes crear ciclos infinitos que generen cadenas de texto estructuradas 
    de forma consecutiva (como números de folio para exámenes o códigos de 
    transacciones) sin temor a saturar el sistema.

    Usar yield para cadenas de texto te ofrece dos grandes ventajas:
    
    1)  Memoria Constante: No importa si el generador va a procesar 3 
        renglones o 5 millones de registros de texto; el consumo de memoria 
        RAM se mantiene plano y bajo porque procesa un solo elemento a la vez.
    2)  Evaluación Perezosa (Lazy Evaluation): El procesamiento de formato del 
        texto solo ocurre en el instante exacto en que el programa principal 
        pide el siguiente dato, optimizando el uso de la CPU.
"""
def generador_folios_examen(prefijo_materia):
    consecutivo = 1
    while True:
                            # Creamos una cadena con formato (ej. POO-0001, 
                            # POO-0002, etc.)
        folio = f"{prefijo_materia}-{consecutivo:04d}"
        yield folio
        consecutivo += 1

                            # Instanciamos el generador para la materia de 
                            # Programación Orientada a Objetos
folios_poo = generador_folios_examen("POO")

                            # Le pedimos folios de forma manual usando la 
                            # función incorporada next()
print(next(folios_poo))     # Salida: POO-0001
print(next(folios_poo))     # Salida: POO-0002
print(next(folios_poo))     # Salida: POO-0003

                            # El generador puede seguir dando folios 
                            # indefinidamente cuando sean requeridos
