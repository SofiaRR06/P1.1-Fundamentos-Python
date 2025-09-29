#Pedimos datos al usuario
nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura en metros: "))

#Mostramos el texto de ejemplo
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

#Mostramos el tipo de cada variable
print(type(nombre))
print(type(edad))
print(type(altura))