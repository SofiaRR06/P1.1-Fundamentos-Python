#Importamos la librería y comprobamos que funciona correctamente
import emoji
print(emoji.emojize("La librería de emojis se ha instalado correctamente :thumbs_up:"))

#Modificamoes el ejercicio del calculo del IMC
altura = float(input("Introduce tu altura en metros: "))
peso = float(input ("Introduce tu peso en kg: "))

def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    if imc < 18.5:
       print("Tienes bajo peso " + emoji.emojize(":warning:", language="alias"))
    elif imc < 25:
        print("Tu IMC es normal" + emoji.emojize(":smile:", language="alias"))
    else:
         print("Tienes sobrepeso" + emoji.emojize(":exclamation:", language="alias"))

#Imprimimos resultados
calcular_imc(peso, altura)