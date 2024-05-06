#Ejercicio 7: Juego de Adivinar el Número 
#Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo. 
#El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo. El juego debe continuar hasta que el jugador adivine correctamente el número.

import random

def juego_adivinar_numero():
    numero_secreto = random.randint(1, 100)

    while True:
        numero_jugador = int(input("Ingrese el numero secreto: "))

        if numero_jugador > numero_secreto:
            print("El numero es alto, intente mas bajo")
        if numero_jugador < numero_secreto:
            print("El numero es bajo, intente mas alto")
        if numero_jugador == numero_secreto:
            print("ACERTASTE EL NUMEROO!!! Bien jugado <3")
            return False    


if __name__ == "__main__":
    juego_adivinar_numero()
