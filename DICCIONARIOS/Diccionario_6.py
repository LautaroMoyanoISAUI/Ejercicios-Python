
def intercambiar_valores(diccionario1, diccionario2):
    diccionario1_cambiado = {}
    diccionario2_cambiado = {}
    for clave, valor in diccionario1.items():
        diccionario1_cambiado[clave] = diccionario2.get(clave, valor)
    for clave, valor in diccionario2.items():
        diccionario2_cambiado[clave] = diccionario1.get(clave, valor)
    return diccionario1_cambiado, diccionario2_cambiado

diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'a': 3, 'b': 4}

resultado = intercambiar_valores(diccionario1, diccionario2)
print(f"Diccionario intercambiado: {resultado}")
