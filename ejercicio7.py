#Pedimos la lista de números
lista = input("Introduce una lista de números separados por coma: ")

#Convertimos los números a una lista
lista_num = [int(num) for num in lista.split(",")]

#Calculo de la suma
suma = sum(lista_num)
#Calculo del promedio
promedio = suma / len(lista_num)
#Calculo del máximo
maximo = max(lista_num)
#Calculo del mínimo
minimo = min(lista_num)

print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")