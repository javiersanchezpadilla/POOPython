""" OVERWRITTING (Anulación o reemplazo)

    A veces hacemos overwrittig por error
"""
class Calculadora:
    def sumar(self, a, b):
        return a + b

calc = Calculadora()
calc.sumar = 10  # ¡Aquí el alumno hizo OVERWRITING!
# Ahora, si intenta hacer calc.sumar(5, 5), Python dará un error
# porque 'sumar' ya no es un método, sino un simple número (int).

# calc.sumar(5, 5)
