""" SE PUEDE SOBRECARGAR AND, OR Y NOT?

    No directamente para las palabras clave and, or y not.
    En Python, estas tres palabras clave están "cableadas" en el núcleo 
    del lenguaje para trabajar con la lógica booleana y no se pueden 
    sobrecargar. Sin embargo, Python nos ofrece una alternativa elegante 
    a través de los operadores de bits (Bitwise Operators).

    ¿Por qué no se pueden sobrecargar and y or?
    -------------------------------------------
    Python utiliza algo llamado evaluación de cortocircuito (short-circuit 
    evaluation). Por ejemplo, en A and B, si A es falso, Python ni siquiera 
    mira a B. Si permitiera sobrecargar and, se perdería esta optimización 
    tan importante para el rendimiento.

    La solución: Sobrecargar los operadores bit a bit
    -------------------------------------------------
    Para lograr un efecto similar, los programadores de Python sobrecargamos 
    los símbolos de bits. Es una práctica estándar en librerías famosas como 
    Pandas o SQLAlchemy.    

    Operador Lógico     Operador de Bits        Método Mágico a Sobrecargar
        and                 &                   __and__(self, other)
        or                  |                   __or__(self, other)
        not                 ~                   __invert__(self)


    Ejemplo Práctico: Filtros de Selección
    Imagina que estás creando un sistema para filtrar alumnos. Quieres combinar 
    dos filtros: "Que sean de Programación" Y "Que tengan promedio > 9".

    ¿Cuándo usar cada uno?
    ----------------------
    Es importante tomar en cuenta esto para evitar errores:

    **) Usa and / or: Cuando quieras comparar si un objeto existe o es verdadero 
        (Lógica booleana pura).
    **) Usa & / |: Cuando quieras combinar la lógica de dos objetos personalizados 
        (como en nuestro ejemplo de los filtros).

    Un truco:
    Si intentamos usar and con los objetos, Python simplemente revisará si el objeto 
    es None o no. Pero si usan &, Python irá a buscar el método __and__ 
    que nosotros mismo escribimos.
"""

class Filtro:
    def __init__(self, condicion):
        self.condicion = condicion

    # Sobrecargamos el símbolo & para que actúe como un "AND"
    def __and__(self, otro_filtro):
        nueva_condicion = f"({self.condicion} Y {otro_filtro.condicion})"
        return Filtro(nueva_condicion)

    def __str__(self):
        return f"Filtro activo: {self.condicion}"

# --- Uso en clase ---
f1 = Filtro("Materia == 'Programación'")
f2 = Filtro("Promedio >= 90")

# Usamos & en lugar de 'and'
filtro_combinado = f1 & f2 

print(filtro_combinado) 
# Resultado: Filtro activo: (Materia == 'Programación' Y Promedio >= 90)
