"""Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas."""

def ordenar_lista(lista):
    return sorted(lista, key=lambda x: x.lower())


lista = ["Zorro", "Gato", "perro", "elefante"]
lista_ordenada = ordenar_lista(lista)

print(lista_ordenada)