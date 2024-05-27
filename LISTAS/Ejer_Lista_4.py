def elementos_mayores(lista, n):
    return [elemento for elemento in lista if elemento > n]


numeros = [5, 10, 15, 20, 25]
n = 11
mayores_que_n = elementos_mayores(numeros, n)
print("Elementos mayores que", n, "son:", mayores_que_n)



    