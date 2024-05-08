"""Ejercicio 10: Juego del Ahorcado 
Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. 
Puedes hacerlo con una lista predefinida de palabras."""

import re

def generar_palabra():
    palabras = [instituto, teclado, tenis, caracol, telefono, procesador, koala, ornitorrinco, perro]
    return random.choice(palabras)

def pedir_letra():
    letra = input("Ingrese una letra: ")
    return letra

def juego_ahorcado():
    palabra = generar_palabra()
    intentos = 5

    




