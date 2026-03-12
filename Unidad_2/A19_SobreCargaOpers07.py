""" TABLA DE RESUMEN DE OPERACIONES A SOBRECARGAR

    REPRESENTACIÓN:
    ---------------
    Operador/Función        Método Mágico               Propósito
    print(obj), str()       __str__(self)       Devuelve una cadena 'bonita'
                                                para el usuario."
    repr(obj)               __repr__(self)      Devuelve una cadena técnica 
                                                para el desarrollador.
    
    ARITMETICOS:
    ------------
    Operador/Función    Método Mágico                   Propósito
    +                   __add__(self, other)        Suma de dos objetos.
    -                   __sub__(self, other)        Resta de dos objetos.
    *                   __mul__(self, other)        Multiplicación.
    /                   __truediv__(self, other)    División decimal.
    //                  __floordiv__(self, other)   División entera.
    %                   __mod__(self, other)        Módulo (residuo).
    **                  __pow__(self, other)        Potencia.
    
    COMPARACIÓN:
    ------------
    Operador/Función    Método Mágico                   Propósito
    ==                  __eq__(self, other)         Igualdad.
    !=                  __ne__(self, other)         Diferencia (No igual).
    <                   __lt__(self, other)         Menor que.
    >                   __gt__(self, other)         Mayor que.
    <=                  __le__(self, other)         Menor o igual que.
    >=                  __ge__(self, other)         Mayor o igual que.
    
    CONTENEDORES:
    -------------
    Operador/Función    Método Mágico                   Propósito
    len(obj)            __len__(self)               Devuelve el tamaño o 
                                                    cantidad de elementos.
    item in obj         __contains__(self, item)    Verifica si un elemento 
                                                    existe dentro.
    obj[key]            __getitem__(self, key)      Permite acceder a datos 
                                                    usando corchetes.
   
    LLAMADA:
    --------
    Operador/Función    Método Mágico                   Propósito
    obj()               __call__(self, ...)         Permite que el objeto se 
                                                    use como una función.


    IMPORTANTE!!!
    -------------
    **) El parámetro other: Casi todos los métodos de operación requieren un 
        segundo parámetro (normalmente llamado other). Este representa al objeto 
        que está a la derecha del operador.
    **) Identidad vs. Valor: Explícales que __eq__ define si los datos son 
        iguales. Si no sobrecargamos este método, Python usa la comparación por 
        defecto, que solo da True si son exactamente el mismo objeto en la misma 
        dirección de memoria.
    **) El método __repr__: Es una buena práctica incluirlo junto a __str__. 
        Mientras que __str__ es para el usuario final, __repr__ ayuda al 
        programador a ver qué hay dentro del objeto cuando lo inspecciona en la 
        consola o en un depurador.                                                    
"""

class GrupoEstudiantes:
    def __init__(self, lista):
        self.alumnos = lista

    def __len__(self):
        return len(self.alumnos)

    def __contains__(self, nombre):
        return nombre in self.alumnos

# Uso:
clase_python = GrupoEstudiantes(["Javier", "Antonio", "Axel"])
print(len(clase_python))      # 3
print("Javier" in clase_python) # True
