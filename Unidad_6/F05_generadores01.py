""" GENERADORES (YIELD).

    Un generador es una función especial en Python, la cual permite regresar 
    una secuencia de valores, pero esta secuencia de valores no se regresan 
    todos los valores al mismo tiempo, sino que por medio de la palabra 
    reservada YIELD (producir), vamos a ir regresando poco a poco los valores
    definidos en una secuencia, de esta manera, entonces ya no vamos a 
    utilizar la palabra RETURN para regresar todos los valores de golpe, sino 
    que vamos a utilizar la palabra reservada YIELD para ir regresando los 
    valores poco a poco de nuestra secuencia de valores que definamos en un 
    generador.
    Un generador es una función especial, en Python retorna una secuencia de 
    valores. pero también suspende la ejecución de  la función por medio de la 
    palabra reservada YIELD con esa palabra reservada evitamos hacer uso de la 
    función RETURN, ya que de lo contrario se estaría regresando el control a 
    la función Ya no se suspende la ejecución de manera temporal y regresa a 
    todos los valores de la secuencia.
    Este generador va a regresar tres valores, pero los va a regresar a 
    demanda cada vez que mandemos a llamar esta función de generador para 
    ello vamos a utilizar la palabra reservada YIELD, .Regresamos un primer 
    valor posteriormente de nueva cuenta, la  palabra reservada YIELD va a 
    regresar un segundo valor y un tercer valor.
    Obviamente, esta secuencia de valores puede ser mucho más grande, pero en 
    este caso solamente estamos realizando tres valores.
"""
def generador():
    yield 1		# en la llamada uno envia el valor 1 y termina la fun.
    yield 2		# en la llamada dos envia el valor 2 y termina la fun.
    yield 3		# en la llamada tres envia el valor 3 y termina la fun.

gen = generador()
print(next(gen))    # genera el 1
print(next(gen))    # genera el 2
print(next(gen))    # genera el 3
