"""Ejercicio 7
Contar letras: Crea una función que tome una cadena como entrada y devuelva un
diccionario con el recuento de cada letra en la cadena."""

def contar_letras(cadena):
    contador_letras = {}
    for letra in cadena:
        if letra != ' ':
            if letra in contador_letras:
                contador_letras[letra] += 1
            else:
                contador_letras[letra] = 1
    
    return contador_letras

def principal():
    cadena = input('Ingrese un texto: ')
    resultado = contar_letras(cadena)

    print(resultado)

principal()

