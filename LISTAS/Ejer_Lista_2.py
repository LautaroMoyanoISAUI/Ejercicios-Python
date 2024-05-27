"""2. Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
valor máximo y el mínimo de la lista."""

def Maximo_Minimo(lista):

    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo

def principal():
    numeros = []

    while True:
        numero = input("Ingrese un numero(O presione enter si no quiere ingresar mas): ")
        if numero:
            numeros.append(float(numero))
        else: 
            maximo, minimo = Maximo_Minimo(numeros)
            print(f"El numero maximo es: {maximo}")
            print(f"El numero minimo es: {minimo}")

principal()