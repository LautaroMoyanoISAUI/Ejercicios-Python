"""Ejercicio 5
Crear una función recursiva que permita calcular el factorial de un número. Realiza un
programa principal donde se lea un número validado como entero, el cual es ingresado por
el usuario y se muestre el resultado del factorial."""

def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n - 1)
    
def principal():

    numero = float(input('Ingrese el numero a factoriar: '))

    if numero < 0:
        print("Ingrese un numero positivo")
        return principal()
    else:
        resultado = calcular_factorial(numero)
        print(f'El factorial de {numero} es igual a: {resultado}')

principal()


    
