""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    CAPTURAR EL ERROR ESPECIFICO SIN MOSTRAR EL MENSAJE ORIGINAL

    Cuándo usar la versión SIN mensaje original
    -------------------------------------------
    Úsalo cuando:
    -------------
    *)  El error es muy obvio (el usuario ya sabe que no se puede dividir 
        entre cero)
    *)  Quieres un programa muy limpio y simple
    *)  Estás aprendiendo y solo quieres saber que el error ocurrió

    No lo uses cuando:
    ------------------
    *)  Necesitas depurar y saber exactamente qué falló
    *)  El mensaje original tiene información útil (como el nombre de archivo)
    *)  El programa es grande y necesitas logs detallados


    ¿Qué mostraría este código?

    Muestra 'Lista muy pequeña' porque el error es IndexError, no 
    ZeroDivisionError.

"""
try:
    numeros = [1, 2, 3]
    print(numeros[10])

except IndexError:
    print("Lista muy pequeña")

except ZeroDivisionError:
    print("División entre cero")
