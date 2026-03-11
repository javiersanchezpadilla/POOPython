""" ¿Cómo se debe comparar? (Regla de Oro)

    Aunque puedes usar == None, la forma profesional y recomendada en Python 
    (PEP 8) es usar el operador de identidad <is>.

        Correcto:       if variable is None:
        Incorrecto:     if variable == None:

    Esto es porque solo existe un único objeto None en toda la memoria de Python 
    durante la ejecución del programa. Todas las variables que son None apuntan 
    exactamente al mismo sitio.
"""
def configurar_arma(self, arma=None):
    if arma is None:
        print("No se seleccionó arma, usando equipo básico.")
    else:
        self.arma = arma

