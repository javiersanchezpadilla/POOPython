""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    CAPTURAR EL ERROR ESPECIFICO SIN MOSTRAR EL MENSAJE ORIGINAL

    Ejemplo: Capturar índice fuera de rango (sin mostrar mensaje)
    En este ejemplo No le decimos al usuario 'IndexError: list index out of 
    range' (mensaje técnico propio de Python), solo le decimos 'índice fuera 
    de rango' (mensaje humano, personalizado y amigable).

"""
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    
    except IndexError:
        print("El índice está fuera del rango de la lista")
        return None


           # 0   1   2  <-- Valores de los índices de la lista mi_lista
mi_lista = [10, 20, 30]                     # mi lista tiene del índie 0 al 2
elemento = obtener_elemento(mi_lista, 5)    # Muestra El índice está fuera del
                                            # rango de la lista
print(f"Resultado: {elemento}")             # Resultado: None
