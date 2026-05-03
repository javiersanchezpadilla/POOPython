""" MANEJO DE EXCEPCIONES.

    Excepciones Personalizadas (Nivel Avanzado)
    -------------------------------------------
    A veces se requieren o necesitamos errores que Python no tiene por defecto
    Por ejemplo, una excepción si un alumno intenta inscribirse a una materia 
    sin haber cursado la anterior (pre-requisito).

    El Principio EAFP (Estilo Python)
    ---------------------------------
    En otros lenguajes se usa mucho el 'mirar antes de saltar' (LBYL - Look 
    Before You Leap), llenando todo de if.
    En Python, enseñamos el EAFP (Easier to Ask for Forgiveness than 
    Permission):

    *)  No hagas esto: if archivo_existe: abrir()
    *)  Haz esto: try: abrir() except FileNotFoundError: ...

¿Por qué? Porque es más eficiente y evita problemas de "concurrencia" (donde el archivo existe cuando lo revisas, pero alguien lo borra un milisegundo antes de que lo abras).
"""
# Definimos nuestra propia excepción heredando de la clase base
class ErrorPreRequisito(Exception):
    def __init__(self, materia_faltante):
        self.mensaje = f"No puedes cursar esta materia sin antes aprobar: {materia_faltante}"
        super().__init__(self.mensaje)

# Uso en la lógica de negocio
def inscribir_materia(tiene_fundam_program):
    if not tiene_fundam_program:
        raise ErrorPreRequisito("Fundamentos de Programación")
    print("¡Inscripción exitosa a Programación Orientada a Objetos!")

try:
    inscribir_materia(tiene_fundam_program=False)
except ErrorPreRequisito as error:
    print(f"Aviso Académico: {error}")
