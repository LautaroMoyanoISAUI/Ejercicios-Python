import random


palabras = palabras = ['python', 'java', 'javascript', 'html', 'css', 'ruby', 'php', 'cocodrilo']
secreta = random.choice(palabras)
cadena = "_" * len(secreta)
print("Bienvenido al juego de ahorcado")
intentos = 0

while True:
    print(cadena)
    letra = (input("Ingrese una letra: ")).lower()
    if letra in secreta:
        for i in range(len(cadena)):
            if secreta[i] == letra:
                cadena = cadena[:i] + letra + cadena[i+1:]
    else:
        intentos += 1
        if intentos == 1:
            print("O")
        elif intentos == 2:
            print(" O")
            print("/")
        elif intentos == 3:
            print(" O")
            print("/|")
        elif intentos == 4:
            print(" O")
            print("/|\\")
        elif intentos == 5:
            print(" O")
            print("/|\\")
            print("/")
        elif intentos == 6:
            print(" O")
            print("/|\\")
            print("/\\")
            print(f"Perdiste! La palabra secreta era {secreta}")
            break
    if cadena == secreta:
        print(f"Ganasteee!! La palabra secreta era {secreta}")
        break
    

            
