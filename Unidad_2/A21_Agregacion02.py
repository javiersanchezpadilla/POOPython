""" En términos sencillos: La agregación es un tipo de relación entre dos clases 
    donde una clase "tiene" o "se compone de" objetos de otra clase, pero con 
    una característica vital: los objetos pueden existir de forma independiente.

    Puntos clave:
    -------------

    1. La relación "Tiene un..." (Has-a)
    A diferencia de la herencia (que es una relación "Es un"), la agregación describe
    pertenencia.
        1)  Un Departamento 'tiene' Profesores.
        2)  Un Carrito de Compras 'tiene' Productos.

    2. La Regla de Independencia
    Esta es la parte que más confunde a los alumnos. En la agregación, si el "contenedor" 
    (el objeto principal) se destruye, los objetos que estaban dentro siguen existiendo.

    Ejemplo práctico:
    Si la Universidad cierra (se elimina el objeto Universidad), los Profesores 
    (objetos Profesor) no dejan de existir en el mundo real; simplemente ya no están 
    asociados a esa universidad. Pueden irse a otra.


"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []     # Aquí ocurre la AGREGACIÓN

    def agregar(self, producto):
        self.productos.append(producto)

                                # 1. Creamos los productos por separado
p1 = Producto("Laptop", 1500)
p2 = Producto("Mouse", 20)

                                # 2. Los agregamos al carrito
mi_carrito = Carrito()
mi_carrito.agregar(p1)
mi_carrito.agregar(p2)

                                # 3. Si borramos el carrito...
del mi_carrito

                                # 4. ¡El producto p1 sigue vivo y disponible!
print(p1.nombre)
