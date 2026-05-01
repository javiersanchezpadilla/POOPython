""" PATRONES DE DISEÑO (CREACIONAL)

    Vamos a llevar Este concepto Singleton (solo 1 objeto) a lo que en 
    ingeniería llamamos un Multiton o un Pool de Recursos.
    Imagina que estás diseñando un sistema para una oficina con 3 impresoras. 
    No quieres que cada empleado cree una impresora virtual nueva cada vez 
    que quiera imprimir, sino que el sistema les asigne una de las 3 
    impresoras físicas que ya existen.

    Código para limitar la creación a exactamente 3 instancias:

    ¿Qué está pasando aquí?
    -----------------------
    1)  Control de Inventario: En lugar de una sola variable _instancia, 
        usamos una lista _instancias.
    2)  La Lógica de Selección: El método __new__ se convierte en un 
        administrador. Si hay espacio en la lista, fabrica un objeto; si no, 
        busca en su lista y te presta uno que ya fabricó antes.
    3)  Balanceo de Carga: Al usar (cls._contador + 1) % cls._limite, estamos 
        haciendo que el sistema sea justo: si pides una cuarta impresora, te 
        da la primera; si pides una quinta, te da la segunda, y así 
        sucesivamente.

    Aplicación en Ingeniería de Sistemas
    Este patrón es vital para el rendimiento de servidores. Crear objetos de 
    Conexión a Base de Datos es costoso (consume mucha memoria y tiempo). En 
    lugar de crear miles de conexiones, los ingenieros crean un Pool de 10 
    conexiones y las reutilizan mediante este patrón.

    Al final __new__ nos da el poder de decidir si el usuario realmente recibe 
    un objeto nuevo o uno reciclado.
"""
class GestionImpresoras:
    _instancias = []  # Lista para guardar nuestras 3 impresoras
    _limite = 3       # El número máximo de objetos permitidos
    _contador = 0     # Para ir rotando entre ellas (Round Robin)

    def __new__(cls, *args, **kwargs):
        # 1. Si aún no llegamos al límite, creamos una nueva
        if len(cls._instancias) < cls._limite:
            nueva_instancia = super(GestionImpresoras, cls).__new__(cls)
            cls._instancias.append(nueva_instancia)
            print(f"--- Creando Impresora Física #{len(cls._instancias)} ---")
            return nueva_instancia
        
        # 2. Si ya llegamos al límite, entregamos una de las existentes
        # Usamos el contador para repartir el trabajo (una vez cada una)
        print(f"--- Límite alcanzado. Asignando Impresora existente #{cls._contador + 1} ---")
        instancia_asignada = cls._instancias[cls._contador]
        
        # Rotamos el contador: 0, 1, 2 y vuelve a 0
        cls._contador = (cls._contador + 1) % cls._limite
        
        return instancia_asignada

# --- PRUEBA EN EL LABORATORIO ---

# Creamos 5 objetos de "impresora"
impresoras_empleados = [GestionImpresoras() for _ in range(5)]

# Verificamos cuáles son iguales
print(f"\n¿La impresora 1 y la 4 son la misma? {impresoras_empleados[0] is impresoras_empleados[3]}")
print(f"¿La impresora 2 y la 5 son la misma? {impresoras_empleados[1] is impresoras_empleados[4]}")
