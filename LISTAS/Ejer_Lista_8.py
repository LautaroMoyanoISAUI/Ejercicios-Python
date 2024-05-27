"""Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
que sea la concatenación de ambas."""

def concatenar_listas(lista1, lista2):
    lista_concatenada = lista1 + lista2
    return lista_concatenada


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]


resultado = concatenar_listas(lista1, lista2)
print(resultado)
