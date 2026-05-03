""" MANEJO DE EXCEPCIONES

    Manejo de bloques try except dentro de un mismo programa.
    Para comprender esto, lo mejor es usar un ejemplo de un proceso por etapas
    En ingeniería, es muy común tener un flujo donde cada paso puede fallar 
    por razones distintas y queremos manejar cada uno de forma independiente 
    para que el programa no se detenga por completo.

    Un escenario ideal es un Procesador de Datos Académicos que:
    ------------------------------------------------------------
    1)  Solicita una calificación (posible error de entrada).
    2)  Realiza un cálculo matemático complejo (posible error de cálculo).
    3)  Guarda el resultado en un archivo (posible error de sistema/disco).

    Sistema de Procesamiento de Actas   

    Es fundamental entendr por qué usamos varios bloques en lugar de uno solo 
    gigante:
    1)  Independencia de Errores: Si el Bloque 1 falla (el usuario mete una 
        letra), el programa no muere; el except le asigna un 0.0 y el código 
        continúa hacia el Bloque 2.
    2)  Manejo Específico: Si metemos todo en un solo try, sería muy difícil 
        saber si el error ocurrió al escribir en el teclado, al calcular o al 
        abrir el archivo. Al separarlos, tenemos control total sobre cada fase.
    3)  Continuidad del Negocio: En sistemas críticos (como los que ellos 
        diseñarán como ingenieros), si el paso de 'Guardar en disco' falla, 
        quizás queremos que el programa siga funcionando en memoria o intente 
        mandarlo por red, en lugar de cerrarse abruptamente.

    ¿Cómo se ve todo esto en la estructura del código?
    ---------------------------------------------------
    Cada try-except actúa como una aduana. El programa intenta cruzarla; si 
    hay un problema, la aduana lo resuelve y lo deja pasar a la siguiente 
    etapa.


    Reflexión final:
    ----------------
    Un buen ingeniero no es el que confía en que su código nunca fallará, sino 
    el que sabe exactamente qué hará su programa cuando el fallo ocurra."

    Resumen de la Unidad de Robustez de Software
    Hasta ahora hemos cubierto:

    1)  Patrones de Diseño: Para que la estructura sea flexible y escalable.
    2)  Manejo de Excepciones: Para que el software sea resistente a errores y 
        fallos externos.

    Con estos dos pilares, pueden enfrentar proyectos mas solidos, como 
    sistemas distribuidos o aplicaciones con bases de datos reales.

    Como recomendación estudien Pruebas Unitarias (Unit Testing) que es el 
    siguiente paso lógico para asegurar la calidad del software o cualquier 
    otro tema de la retícula de Ingeniería en Sistemas Computacionales.

"""
def procesar_acta_academica():
                                        # BLOQUE 1: Entrada de Datos
    try:
        print("Etapa 1: Captura")
        nota = float(input("Ingrese la calificación final: "))
    except ValueError:
        print("Error: Se esperaba un número. Se asignará 0 por defecto.")
        nota = 0.0

                                        # BLOQUE 2: Cálculo de Indicador
    try:
        print("\n--- Etapa 2: Cálculo de Indicador ---")
        # Supongamos que dividimos un factor entre la nota
        factor = 100
        indicador = factor / nota
        print(f"Indicador académico calculado: {indicador:.2f}")
    except ZeroDivisionError:
        print("Advertencia: Nota es 0. El indicador se establecerá en infinito.")
        indicador = float('inf')

                                        # BLOQUE 3: Persistencia (Guardado)
    try:
        print("\n--- Etapa 3: Guardado de Respaldo ---")
        # Intentamos escribir en un directorio que podría no existir o no tener 
        # permisos
        with open("respaldo_actas.txt", "a") as archivo:
            archivo.write(f"Calificación: {nota} - Indicador: {indicador}\n")
        print("Datos guardados en disco exitosamente.")
    except IOError as e:
        print(f"Error de Sistema: No se pudo escribir el archivo. Detalle: {e}")

    print("\n--- Proceso finalizado ---")

# Ejecución del programa
procesar_acta_academica()
