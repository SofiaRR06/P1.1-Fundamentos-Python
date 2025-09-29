import sys
import emoji

def main():
    if len(sys.argv) != 4:
        print("Uso: python calculadora.py <num1> <operador> <num2>")
        print("Ejemplos:")
        print("  python calculadora.py 5 + 3")
        print("  python calculadora.py 10 * 4")
        return

    num_1_str, operador, num_2_str = sys.argv[1], sys.argv[2], sys.argv[3]

#Convertimos los strings de numeros en float y comprobamos que lo introducido es un número
    try:
        num_1 = float(num_1_str)
        num_2 = float(num_2_str)
    except ValueError:
        print(emoji.emojize(":warning:" , language="alias") + "Los números introducidos no son válidos")
        return 
    
 # Hacemos la operación 
    if operador == "+":
        resultado = num_1 + num_2
    elif operador == "-":
        resultado = num_1 - num_2
    elif operador == "*":
        resultado = num_1 * num_2
    elif operador == "/":
        if num_2 == 0:
            print(emoji.emojize(":exclamation:", language="alias") + "No se puede dividir entre cero")
            return
        resultado = num_1 / num_2
    else:
        print(emoji.emojize(":warning:", language="alias") + f"  Operador '{operador}' no reconocido. Usa +, -, * o /")
        return

    # Imprimimos el resultado 
    print(f"El resultado es : {num_1} {operador} {num_2} = {resultado} " + emoji.emojize(":smile:", language="alias"))

if __name__ == "__main__":
    main()