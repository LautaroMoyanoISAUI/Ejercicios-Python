"""Ejercicio 2
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
máximo y el mínimo, utilizando la función anterior."""

def calcularMaxMin(lista):

    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo, minimo

def principal():
    lista = []
    numeros = []

    while True:
        numero = int(input("Ingrese un numero: "))
        numeros.append(float(lista))
        if numero != None:
            maximo, minimo = calcularMaxMin(numeros)
            print(f"El numero maximo es: {maximo}")
            print(f"El numero minimo es: {minimo}")
        else: 
            print("No se ingreso ningun numero")
            break

principal()
    
    
             
        


    