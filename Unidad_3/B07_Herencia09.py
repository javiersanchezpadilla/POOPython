""" HERENCIA

    Herencia con constructor en la subclase usando super() 

    El Sistema de Productos (Lógica Adicional)
    ------------------------------------------
    Imagina un sistema para una tienda. Todos los productos tienen un precio,
    pero los productos importados tienen un impuesto adicional.
"""

class Producto:
    def __init__(self, precio):
        self.precio = precio
        print(f"Producto con precio base: ${self.precio}")

class ProductoImportado(Producto):
    def __init__(self, precio, impuesto):
        # 1. Llamamos al constructor del padre para el precio
        super().__init__(precio)
        # 2. Añadimos la lógica propia del hijo
        self.impuesto = impuesto
        self.precio_final = self.precio + self.impuesto

    def mostrar_total(self):
        print(f"El total con impuestos es: ${self.precio_final}")

# Uso del código
laptop = ProductoImportado(1000, 150)
laptop.mostrar_total()
