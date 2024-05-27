def producto_elementos(lista_numeros):
    producto = 1
    for num in lista_numeros:
        producto *= num
    return producto


numeros_ejemplo = [2, 3, 4, 5]


resultado = producto_elementos(numeros_ejemplo)
print(resultado)
