""" MANEJO DE EXCEPCIONES USANDO CLASES

    Procesador de Inventario de Laboratorio
    ---------------------------------------
    Aquí se maneja la entrada de datos del stock y luego el cálculo de 
    distribución.
"""
class Inventario:
    def procesar_lote(self):
                                            # Entrada de cantidades
        try:
            self.cantidad = int(input("Cantidad de reactivos recibidos: "))
        except ValueError:
            print("Entrada inválida. Se registrará 1 unidad para no frenar el proceso.")
            self.cantidad = 1

                                            # Cálculo de distribución
        try:
            equipos = int(input("Número de equipos de alumnos: "))
            por_equipo = self.cantidad / equipos
            print(f"Cada equipo recibe: {por_equipo} unidades.")

        except ZeroDivisionError:
            print("No hay equipos. El material se queda en almacén.")

        except ValueError:
            print("Error: El número de equipos debe ser un entero.")


lab = Inventario()
lab.procesar_lote()
