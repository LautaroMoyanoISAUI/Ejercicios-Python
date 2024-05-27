def actualizar_diccionario(diccionario, lista_tuplas):
    for clave, valor in lista_tuplas:
        diccionario[clave] = valor
    return diccionario


diccionario_ejemplo = {'a': 1, 'b': 2}
lista_tuplas_ejemplo = [('c', 3), ('d', 4)]
resultado = actualizar_diccionario(diccionario_ejemplo, lista_tuplas_ejemplo)
print(resultado)
