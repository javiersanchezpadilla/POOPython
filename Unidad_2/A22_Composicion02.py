""" COMPOSICION

    Diferencia con la Composición (El "Hermano Estricto")
    Es muy útil contrastarlo con la Composición para que no haya dudas:

        **) Agregación (Débil): El Profesor puede existir sin la Universidad. 
            (Se representa con un rombo vacío en UML <>--).

        **) Composición (Fuerte): El Corazón no puede existir sin el Cuerpo. 
            Si el Cuerpo muere, el Corazón también. (Se representa con un rombo 
            lleno en UML).

    Analogía:
    Imaginen un Estacionamiento y los Autos. El estacionamiento tiene autos (Agregación). 
    Si mañana demolemos el estacionamiento, los autos simplemente se van manejando a otro 
    lado. No se destruyen con el edificio.

    Actividad: "¿Se queda o se va?" (10 Minutos)
    --------------------------------------------
    1. El Reto (5 min)
    Decidir si la relación es Agregación (El objeto menor sobrevive) o Composición (
    El objeto menor desaparece si el mayor se destruye).

    Relación                                ¿Qué pasa si borramos el Objeto A?          ¿Es Agregación o Composición?
    -----------------------------------------------------------------------------------------------------------------
    A: Librero / B: Libros                  ¿Los libros siguen existiendo?                          Agregación
    A: Edificio / B: Pisos                  ¿Los pisos pueden existir sin el edificio?              Composición
    A: Equipo de Fútbol / B: Jugadores      ¿Los jugadores pueden irse a otro equipo?               Agregación
    A: Bosque / B: Árboles                  ¿Si quemamos el bosque, quedan los árboles?"            Composición 
    A: Computadora / B: Monitor Externo     ¿El monitor funciona en otra PC?                        Agregación

    La Discusión "Semi-Técnica"
    ---------------------------

    En la Agregación: "¿Cómo le pasamos los libros al librero?".
    Respuesta esperada: "Se los pasamos como parámetros al constructor o a un método (vienen de fuera)".

    En la Composición: "¿Dónde se crean los pisos del edificio?".
    Respuesta esperada: "Se crean dentro del constructor del edificio (nacen ahí)".

    3. Ejemplo rápido de código para comparar:
    Agregación (Los objetos vienen de fuera):

            # El monitor ya existe antes que la PC
            mi_monitor = Monitor("Dell") 
            # Se lo "entregamos" a la PC
            mi_pc = Computadora(mi_monitor) 
            Composición (El objeto nace dentro):

    class Edificio:
            def __init__(self):
                # El piso se crea AQUÍ adentro, no existe fuera.
                self.piso_1 = Piso(1) 

    Por qué esto ayuda a tu clase:
    Usar agregación, hace que el código seamás flexible (pueden reutilizar objetos en diferentes partes).
    Si usan Composición, su código será más seguro (los objetos internos están protegidos y controlados 
    totalmente por la clase principal).
"""