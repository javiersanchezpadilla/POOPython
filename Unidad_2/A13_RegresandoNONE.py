""" RETORNANDO VALORES DESDE UNA CLASE

    De igual forma que podemos retornar valores desde una función, podemo
    retornar valores desde los métodos mediante el uso de return
    Ejemplo con la clase calculadora.
    La clase tiene dos métodos:
    suma()          imprime el valor pero no lo retorna
    multiplica()    El método retorna el valor

    Creamos una instancia para poder llamar a estos métodos para ver la 
    diferencia.

    el método .suma(), cuando es llamado este método el valor es impreso pero
    un valor None es regresado debido a que no existe una instrucción 'return'
    esto es exactamente lo mismo que esperariamos de una funcion que no tenga
    definido el return

        print(c1.sumar(10, 20))
            30 
            None

    el método .multiplicar(), cuando es llamado al tener retorno de valor, 
    regresa el resultado de la operación.

        print(calculadora.multiplicar(5, 6))

    No vemos None porque estamos regresando un valor en lugar de imprimirlo, este
    valor puede asigmarse a una variable y usarlo posteriorment en el programa.
 """

class Calculadora:
 
    def sumar(self, a, b):
        print(a + b)
 
    def multiplicar(self, a, b):
        return a * b


c1 = Calculadora()

# En este ejemplo se imprimira el valor de la suma de 10 + 20, pero 
# al no tener retorno de valor el valor impreso es None
print('La suma de dos valores')
print(c1.sumar(10, 20))

# Llamamos al metodo multiplicar, donde se tendremos valor de retorno
print('El producto de dos valores')
print(c1.multiplicar(10, 4))
