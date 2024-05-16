#Ejercicio 9: Calculadora de Factorial 
#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. 
#El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. 
#El programa debe manejar números enteros grandes y mostrar el resultado.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    numero = int(input("Ingrese el numero a factoriar: "))

    if numero < 0:
        print("Pon un numero en positivo")
        return main()
    else:
        resultado = factorial(numero)
        print("El resultado de su factorial es: ", resultado)  

if __name__ == "__main__":
    main()  



