def encontrar_indice(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

lista_ejemplo = [3, 7, 2, 9, 4, 5]
valor_buscar = 9
resultado = encontrar_indice(lista_ejemplo, valor_buscar)
print(resultado)
