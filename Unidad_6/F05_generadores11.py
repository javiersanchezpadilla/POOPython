""" GENERADORES DE TEXTOS

    los generadores basados en yield son herramientas sumamente potentes para 
    procesar y producir texto, especialmente cuando trabajas con volúmenes 
    grandes de información.

    En lugar de construir una lista enorme de cadenas de texto en la memoria 
    RAM y regresarla toda de golpe con un return, un generador va entregando 
    línea por línea o palabra por palabra a demanda, usando solo el espacio de 
    memoria de la cadena actual.

    Analogía: El dispensador de tickets vs. Un libro completo
    ----------------------------------------------------------
    **) Con return (Enfoque tradicional): Es como si imprimieras un libro 
        completo de 500 páginas en la memoria y se lo entregaras al usuario de 
        un solo golpe. Si el usuario solo quería leer el primer capítulo, 
        gastaste papel y memoria innecesariamente.
    **) Con yield (Generador): Es como un dispensador de tickets en el banco. 
        Te da un ticket (una línea de texto), se detiene y espera a que pidas 
        el siguiente. No genera el segundo ticket hasta que tú se lo solicites 
        de manera explícita.

    Ejemplo 1 Generador de Reportes de Alumnos (Básico)
    ---------------------------------------------------
    Imagina que tienes una base de datos o una lista y quieres generar un 
    formato de texto estructurado para cada alumno, pero quieres procesarlos 
    uno por uno.
"""
def generador_reportes(lista_alumnos):
    print("[Generador] Iniciando el procesamiento de datos...")
    for alumno in lista_alumnos:
                            # Formateamos el texto para este alumno específico
        reporte_texto = f"REPORTE | Matrícula: {alumno['id']} | Nombre: {alumno['nombre']} | Estatus: Regular"
        
                            # Pausamos la función y enviamos este texto al 
                            # ciclo externo
        yield reporte_texto
        print("[Generador] Reanudando para el siguiente elemento...")


                            # Datos de prueba
alumnos = [
    {"id": "20120001", "nombre": "Carlos"},
    {"id": "20120002", "nombre": "Ana"},
    {"id": "20120003", "nombre": "Luis"}
]

                            # Creamos la instancia del generador (aquí adentro 
                            # no se ha ejecutado nada aún)
mi_dispensador = generador_reportes(alumnos)

print("Iniciando el ciclo de consumo:\n")
                            # Consumimos el generador usando un ciclo for común
for reporte in mi_dispensador:
    print(f"Consumidor recibió: {reporte}\n")
