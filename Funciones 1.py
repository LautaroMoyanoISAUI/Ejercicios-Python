"""Ejercicio 1
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t
ú “. Crea un programa principal donde se use dicha función luego del ingreso del usuario."""

def ConvertirEspaciado (texto):
    texto_espaciado = ""
    for letra in texto:
        texto_espaciado += letra + ' '
    
    return texto_espaciado

def principal():

    texto = input("Ingrese el texto que desea espaciar: ")
    print(ConvertirEspaciado(texto))


principal()


    