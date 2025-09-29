#Función saludar
def saludar(nombre):
    return f"Hola, {nombre}"

#Funcion calcular IMC
def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    return imc

#Pedimos los datos como en el ejercicio 1
nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura en metros: "))
peso = float(input ("Introduce tu peso en kg: "))

#Mostramos resultados llamando a la función
print(saludar(nombre))
print(f"Tu IMC es: {calcular_imc(peso, altura)}")