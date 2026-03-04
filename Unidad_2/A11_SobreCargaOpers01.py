""" Sobre carga de operadores o de métodos especiales.

    Cuando modificamos el comportamiento de métodos como __str__, __len__ o 
    __add__ dentro de nuestra propia clase, el término técnico más preciso 
    es Sobrecarga de Operadores (o Operator Overloading) o, de forma más 
    general, Sobreescritura de Métodos Especiales.

    ¿Por qué "Sobrecarga de Operadores"?
    ------------------------------------
    Se llama así porque los métodos mágicos permiten que los operadores comunes 
    de Python (como +, -, *, o funciones como print() y len()) funcionen con 
    tus propios objetos.
    **) Si usas + con números, los suma.
    **) Si usas + con strings, los concatena.
    **) Si sobrecargas __add__, puedes hacer que + sume dos Naves o dos Dragones. 
        Estás "cargando" al operador con un nuevo significado.

    Ejemplo Práctico: El método __str__

    Este método es el encargado de decidir qué se muestra cuando haces un 
    print(objeto). Si no lo sobrecargas, Python muestra una dirección de memoria fea.

    Diferencia entre los nombres.
    -----------------------------
    Es común que en clase se confundan estos términos, aquí tienes la distinción:

    **) Sobreescritura (Overriding): Es lo que hacemos técnicamente. El método 
        __str__ ya existe en la clase base de Python (llamada object). 
        Al escribirlo en tu clase, estás "escribiendo encima" de la versión original.
    **) Sobrecarga (Overloading): Es el efecto que logramos. Estamos haciendo que 
        funciones estándar de Python se comporten de forma especial para nuestra clase.

     Otros métodos mágicos comunes para sobrecargar:
     
     Operador / Función     Método Mágico   Uso Práctico
     print(obj)               __str__       Presentación bonita para el usuario.
     len(obj)                 __len__       Para decir cuántos ítems tiene tu objeto.
     obj1 + obj2              __add__       Para sumar dos objetos personalizados.
     obj1 == obj2             __eq__        Para definir cuándo dos objetos son "iguales".

     "Si tenemos una clase Libro, ¿qué debería devolver el método __len__? 
     ¿El número de páginas o el número de letras?"
"""

class Nave:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

                        # SOBRECARGA / SOBREESCRITURA del método mágico
    def __str__(self):
        return f"Nave: {self.nombre} (Modelo: {self.modelo})"


mi_nave = Nave("Halcón", "Carguero Corelliano")
print(mi_nave)          # Al imprimir, Python busca automáticamente el método __str__
