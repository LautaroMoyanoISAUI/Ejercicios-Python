"""Ejercicio 10: Juego del Ahorcado 
Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. 
Puedes hacerlo con una lista predefinida de palabras."""


import random

def seleccionar_palabra():
    palabras = ['python', 'java', 'javascript', 'html', 'css', 'ruby', 'php', 'cocodrilo']
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    palabra_mostrada = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += '_'
    return palabra_mostrada

intentos = 6
letras_adivinadas = []
palabra_secreta = seleccionar_palabra()

print("¡Bienvenido al Juego del Ahorcado!")
print("Tienes que adivinar la palabra antes de que se agoten los intentos.")
print(f"La palabra tiene {len(palabra_secreta)} letras: {mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)}")

while intentos > 0:
    letra = input('Ingrese una letra: ')
    letras_adivinadas.append(letra)
    
    if letra not in palabra_secreta:
        print("Letra incorreta!")
        intentos -= 1
        print('Te quedan ', intentos, 'intentos.')
    else:
        print('Letra Correcta!!')

    palabra_mostrada = mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)
    print(palabra_mostrada)
    if '_' not in palabra_mostrada:
        print("¡Felicidades! ¡Adivinaste la palabra!")
        break

if intentos == 0:
    print("NoooooOoOoOo!! Te quedaste intentos. La palabra era:", palabra_secreta)


        

    





    




