def filtrar_diccionario(diccionario, lista_claves):
    diccionario_filtrado = {}
    for clave in lista_claves:
        if clave in diccionario:
            diccionario_filtrado[clave] = diccionario[clave]
    return diccionario_filtrado

# Ejemplo de uso
mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
claves_a_filtrar = ['a', 'c']

diccionario_filtrado = filtrar_diccionario(mi_diccionario, claves_a_filtrar)
print(diccionario_filtrado)