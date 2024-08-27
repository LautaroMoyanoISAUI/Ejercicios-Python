def sacar_puntos_comas(lista):
    list(lista)
    if lista[-1] == "." or lista[-1] == ",":
        lista = lista[:-1]
        return lista
    else:
        return lista  

def contar_palabras(lista):
    diccionario = {}
    for i in range(len(lista)):
        lista_simple = lista[i].split()
        for palabra in lista_simple:
            palabra = palabra.lower()
            palabra = sacar_puntos_comas(palabra)
            if palabra not in diccionario:
                diccionario[palabra] = 1
            else:
                diccionario[palabra] += 1
    return diccionario

frases = ("Hola, ¿cómo estás?","hola¡Qué día tan bonito!","Gracias por tu ayuda.")
print(contar_palabras(frases))