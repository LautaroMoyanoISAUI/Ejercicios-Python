def sumar_valores(diccionario):
    suma = sum(diccionario.values())
    return suma

# Diccionario de ejemplo
diccionario_ejemplo = {
    'a': 10,
    'b': 20,
    'c': 30
}

# Llamada a la función con el diccionario de ejemplo
resultado = sumar_valores(diccionario_ejemplo)
print(resultado)
