def combinar_diccionarios(diccionario1, diccionario2):
    diccionario_combinado = {}
    for key, value in diccionario1.items():
        diccionario_combinado[key] = value
    for key, value in diccionario2.items():
        diccionario_combinado[key] = value
    return diccionario_combinado


diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {1: 'a', 2: 'b', 3: 'c'}
diccionario_combinado = combinar_diccionarios(diccionario1, diccionario2)
print(diccionario_combinado)
