"""Inventario de productos : Escribe una función que recibe un diccionario donde las claves son los nombres 
de los productos y los valores son listas de precios históricos de esos productos. 
La función debe devolver un nuevo diccionario donde las claves son los nombres de los 
productos y los valores son el precio promedio de cada producto."""

def inventario_productos(diccionario_p):
    diccionario_productos = {}
    promedio = 0

    for clave, valor in diccionario_p.items():
        promedio = sum(valor) / len(valor)
        diccionario_productos[clave] = diccionario_p[clave]
        diccionario_productos[clave] = promedio
    return diccionario_productos


diccionario_p = {
    "lechuga": [200, 100, 300],
    "papa": [100,300,130],
    "banana": [230,456,100]
}
resultado = inventario_productos(diccionario_p)
print(resultado)