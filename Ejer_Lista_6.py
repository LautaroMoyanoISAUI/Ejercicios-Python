def contar_elementos(lista, n):
    contar_numero = 0
    for numero in lista:
        if numero == n:
            contar_numero += 1
    
    return contar_numero

def principal():
    numeros = [5, 10, 15, 15, 15, 25]
    n = 15
    numero_contado = contar_elementos(numeros, n)
    print(f"El numero {n} aparecio {numero_contado} veces")

principal()
