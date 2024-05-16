"""Ejercicio 6
Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
los números pares en la lista."""

def sumar_pares(numeros):
    par = 0
    suma = 0
    for numero in numeros:
        if numero % 2 == 0:
            par = numero
            suma += par
    return suma

def principal():
    numeros = []
    while True:
        numero = input('Ingresa un numero(o presiona enter si desea finalizar la lista): ')
        if numero:
            numeros.append(float(numero))
        else: 
            suma = sumar_pares(numeros)
            print(f'La suma de los numero pares es {suma}')
            break

principal()
    
        
