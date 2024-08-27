"""Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva
 un diccionario donde las claves son las letras iniciales de las palabras 
 y los valores son listas de palabras que comienzan con esa letra."""

def palabra_por_inicial(lista_palabras):
    diccionario_iniciales = {}
    for palabra in lista_palabras:
        letra_inicial = palabra[0].lower()
        if letra_inicial in diccionario_iniciales:
            diccionario_iniciales[letra_inicial].append(palabra)
        else:
            diccionario_iniciales[letra_inicial] = [palabra]
    return diccionario_iniciales



lista_palabras = ["arbol" "luna", "montaña", "río", "casa", "libro", "gato", "perro", "sol", "mar", "araña"]

resultado = palabra_por_inicial(lista_palabras)

print(resultado)




        


