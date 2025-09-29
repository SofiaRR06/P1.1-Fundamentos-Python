# Definimos la función
def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    
    # Por si no introduce la edad
    if edad is None:
        mensaje = f"{nombre} no ha introducido su edad"
    else:
        mensaje = f"{nombre} tiene {edad} años"
    
    # Por si no tiene aficiones
    if aficiones:
        mensaje += " y le gusta: " + ", ".join(aficiones)
    else:
        mensaje += " y no tiene aficiones"

    print(mensaje)


# Ejemplos de uso

presentar_persona("Ana", 25, "leer", "correr", "viajar")

presentar_persona()