def diccionario_inverso(diccionario):
    diccionario_invertido = {}
    for clave, valor in diccionario.items():
        diccionario_invertido[valor] = clave
    return diccionario_invertido


diccionario_ejemplo = {'a': 1, 'b': 2, 'c': 3}
diccionario_invertido = diccionario_inverso(diccionario_ejemplo)
print(diccionario_invertido)
