"""Ejercicio 8
Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
de puntuación."""

def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    
    primer_letra = 0
    ultima_letra = len(palabra) - 1
    for i in range(0, len(palabra)):
        if palabra[primer_letra] == palabra[ultima_letra]:
            primer_letra += 1
            ultima_letra -= 1
        else: 
            return False
    return True

palabra = input("Ingrese una palbra o frase: ")

if palindromo(palabra):
    print("Es una palabra o frase Palindroma")
else:
    print("No es palindroma")



    
    
    
    
    