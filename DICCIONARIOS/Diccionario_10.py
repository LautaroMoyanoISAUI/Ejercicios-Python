def valores_unicos(diccionario):
    valores_unicos = list(set(diccionario.values()))
    return valores_unicos


diccionario_ejemplo = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
resultado = valores_unicos(diccionario_ejemplo)
print(resultado)
