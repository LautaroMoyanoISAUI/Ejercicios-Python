def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    else:
        return sum(lista) / len(lista)

def principal():
    numeros = []
    while True:
        numero = input("Ingrese un numero o presione enter para finalizar la lista: ")
        if numero:
            numeros.append(float(numero))
        else:
            resultado = calcular_promedio(numeros)
            print(f"El promedio es igual a: {resultado}")

principal()