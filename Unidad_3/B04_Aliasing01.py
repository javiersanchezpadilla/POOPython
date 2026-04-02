""" ALIASING (DIFERENTE NOMBRE, MISMO OBJETO)

    Son dos a mas referencias a la misma dirección de memoria dentro del 
    mismo programa.

"""
a = [6, 2, 4, 7, 1]     # Creamos el objeto lista y le llamamos 'a'
b = a                   # asignamos a 'b' la misma dirección de 'a'
                        # incluso podriamos tener mas alias
                        # c = b   d = c   e = d (no es recomendado pero
                        # funciona), al final es algo como el mismo objeto
                        # pero con distintos nombres (alias)

print(id(a))            # Podemos comprobar que tienen la misma dirección
print(id(b))            # de memoria ambos objetos.

print(a is b)           # Son la misma referencia al mismo objeto