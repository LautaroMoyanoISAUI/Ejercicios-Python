def diccionario_listas(diccionario):
    valores = diccionario.values()
    lista_valores = []
    for lista in valores:
        for elemento in lista:
            lista_valores.append(elemento)
    return lista_valores


diccionario = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
resultado = diccionario_listas(diccionario)
print(resultado)
