def contar_letras(cadena):
    frecuencia_letras = {}
    
    for letra in cadena:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1
    
    return frecuencia_letras

cadena_ejemplo = "software"
resultado = contar_letras(cadena_ejemplo)
print(resultado)
