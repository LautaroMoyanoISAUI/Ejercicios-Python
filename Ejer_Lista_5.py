def eliminar_duplicados(lista):
    return list(set(lista))


numeros = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = eliminar_duplicados(numeros)
print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)
