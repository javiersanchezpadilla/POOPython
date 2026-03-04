"""

    Los decoradores son sorprendentes, obtenemos la misma funcionalidad que 
    cuando utilizamos la función de propiedad (property), pero con una sintaxis 
    mucho más concisa.
    Sólo tenemos que escribir añadir propiedad y un proceso especial se iniciará 
    entre bastidores.

    ¿QUÉ ES UN DECORADOR?  

    Un decorador es básicamente una función que toma una función como argumento 
    y amplía su comportamiento sin modificarla explícitamente.
    Por eso lo llamamos decorador, es algo así cómo decorar otra función ampliando 
    su comportamiento, pero no modifica explícitamente la función, sólo añade algo 
    más de sabor o funcionalidad a la función.
    También utilizaremos el nombre de la propiedad si utilizamos el decorador Añadir 
    propiedad, así evitamos añadir nuevos nombres como el nombre del getter y el 
    nombre del setter a nuestra lista de nombres válidos en la clase.

    GETTER.

            @property
            def property_name(self):
                return self._property_name

"""

# VOY EN LA LECCION 75 THE @PROPERTY DECORATOR