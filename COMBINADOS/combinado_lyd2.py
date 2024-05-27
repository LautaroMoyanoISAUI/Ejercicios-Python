def longitud(lista):
    diccionario = {}
    for elemento in lista:
        letras = len(list(elemento))
        if letras not in diccionario:
            diccionario[letras] = [elemento] 
        else:
            diccionario[letras].append(elemento)
    return diccionario

palabras = ("Gato","gato","Lápiz","Sol","Felicidad")
print(longitud(palabras))