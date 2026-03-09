""" El nivel "Pro": Usar *args (Argumentos Variables)
    Si quieres que tu método reciba cualquier cantidad de números, usamos el 
    asterisco *. Esto es lo más cercano a una sobrecarga infinita.
"""
class SuperSumador:

    def sumar(self, *numeros):
        # 'numeros' llega como una lista (tupla) de todo lo que enviamos
        total = sum(numeros)
        print(f"La suma de los {len(numeros)} elementos es: {total}")


s = SuperSumador()
s.sumar(10, 20)                     # Suma de 2
s.sumar(5, 5, 5, 5, 5)              # Suma de 5
s.sumar(5, 5, 5, 5, 5, 5, 5, 5, 5)  # Suma de 95
