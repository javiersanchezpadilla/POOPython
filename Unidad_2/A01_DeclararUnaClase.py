""" En este ejercicio se declarará una clase de forma muy simple"""

class MiClase:
    pass

class OtraClase():
    pass


a = MiClase()
b = MiClase()
c = OtraClase()

            # Mostrar información sobre las clases
print(a)                # <__main__.MiClase object at 0x782245d02030>
print(b)                # <__main__.MiClase object at 0x782245d01fd0>
print(c)                # <__main__.OtraClase object at 0x782245d01fa0>

            # Imprimimos el tipo al que pertenece la clase
print(type(a))          # <class '__main__.MiClase'>
print(type(b))          # <class '__main__.MiClase'>
print(type(c))          # <class '__main__.OtraClase'>

            # Verificamos quien es instancia de quien
print('el objeto "a" es una instancia de MiClase?', isinstance(a, MiClase))
print('el objeto "a" es una instancia de OtraClase?', isinstance(a, OtraClase))

print('el objeto "b" es una instancia de MiClase?', isinstance(b, MiClase))
print('el objeto "b" es una instancia de OtraClase?', isinstance(b, OtraClase))

print('el objeto "c" es una instancia de MiClase?', isinstance(c, MiClase))
print('el objeto "c" es una instancia de OtraClase?', isinstance(c, OtraClase))

            # Imprimimos el identificador de cada clase
            # cada objeto comparte una direccion independiente
print('El identificador del objeto "a" es -->', id(a))
print('El identificador del objeto "b" es -->', id(b))
print('El identificador del objeto "c" es -->', id(c))

print('\n Igualamos los objetos "a" y "b"')
a = b
print('El identificador del objeto "a" es -->', id(a))
print('El identificador del objeto "b" es -->', id(b))
