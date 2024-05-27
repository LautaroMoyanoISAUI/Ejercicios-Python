"""1. Suma de elementos: Escribe una función que tome una lista de números y devuelva la
suma de todos los elementos en la lista."""

def suma_elementos(lista):
    lista_sumada = sum(lista)
    return lista_sumada


def principal() :
    numeros = []
    while True:
        numero = input('Ingresa un numero(o presiona enter si desea finalizar la lista): ')
        if numero:
            numeros.append(float(numero))
        else:
            suma = suma_elementos(numeros)
            print(f"La suma de los numeros en la lista es: {suma}" )
            break

principal()

