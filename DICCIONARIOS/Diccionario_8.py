def diccionario_frecuencias(lista):
    diccionario_frecuencias = {}
    for elemento in lista:
        elemento = elemento.lower()
        if elemento not in diccionario_frecuencias:
            diccionario_frecuencias[elemento] = 1
        else:
            diccionario_frecuencias[elemento] +=1
    return diccionario_frecuencias

palabras = ["hola", "hola", "chau", "hola", "bien", "chau"]
print(diccionario_frecuencias(palabras))




