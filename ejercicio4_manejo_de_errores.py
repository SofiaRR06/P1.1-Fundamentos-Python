#Pedimos el nombre al usuario
nombre = str(input("Introduce tu nombre: "))

#Hacemos un bucle while para asegurarnos de que introducen los tipos de datos correctos
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        altura = float(input("Introduce tu altura en metros: "))
        break
    except ValueError:
        print("No ha introducido un número, inténtelo de nuevo")

#Mostramos el texto de ejemplo
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

#Mostramos el tipo de cada variable
print(type(nombre))
print(type(edad))
print(type(altura))

