""" PATRON FACTORY (CREACIONAL)

    Fábrica de Conexiones a Base de Datos
    ---------------------------------------
    Ideal para cuando una app debe funcionar con distintos motores de base de 
    datos.
"""
class MySQL:
    def conectar(self): return "Conectado a MySQL"

class SQLite:
    def conectar(self): return "Conectado a SQLite"

class FabricaDB:
    @staticmethod
    def obtener_conexion(motor):
        if motor == "mysql": return MySQL()
        if motor == "sqlite": return SQLite()

# Uso: Cambias de base de datos sin cambiar el código principal.
db = FabricaDB.obtener_conexion("mysql")
print(db.conectar())
