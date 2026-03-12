""" El Reto (20 min)

    Habilitar el encadenamiento: Agregar return self al final de cada uno 
    de los tres métodos (pintar, cargar_gasolina, arrancar).

    Prueba de Fuego: En la parte inferior de su script, deben intentar crear 
    y configurar un auto en una sola línea, así:
    
    mi_auto = Automovil("Ford", "Mustang").pintar("Negro").cargar_gasolina(20).arrancar()
    """
class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Blanco"
        self.combustible = 50
        self.encendido = False

    def pintar(self, nuevo_color):
        self.color = nuevo_color
        print(f"Pintando de {self.color}...")
        return self # <--- Clave del éxito

    def cargar_gasolina(self, cantidad):
        self.combustible += cantidad
        print(f"Cargando {cantidad}L...")
        return self # <--- Clave del éxito

    def arrancar(self):
        self.encendido = True
        print("Motor en marcha.")
        return self # <--- Clave del éxito

    def __str__(self):
        estado = "Encendido" if self.encendido else "Apagado"
        return f"Auto: {self.marca} {self.modelo} | Color: {self.color} | Gas: {self.combustible}L | Estado: {estado}"

# Ejecución fluida (Encadenada)
mi_auto = Automovil("Tesla", "Model 3").pintar("Gris").cargar_gasolina(10).arrancar()

print("\n--- Resultado Final ---")
print(mi_auto)