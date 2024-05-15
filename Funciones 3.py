"""Ejercicio 3
Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
función en un programa principal que lea el radio de una circunferencia y muestre su área y
perímetro"""

#formulas Perímetro = 2(pi) por radio. Área = pi por radio al cuadrado.
import math


def calcular_area_perimetro(radio_circunferencia):

    perimetro = (2 * math.pi) * radio_circunferencia
    area = math.pi * (radio_circunferencia ** 2)

    return perimetro, area

def principal():

    radio_circunferencia = float(input("Ingrese el radio de circunferencia: "))
    perimetro, area = calcular_area_perimetro(radio_circunferencia)

    print(f"El perimetro de su circunferencia es igual a: {perimetro} y su area es igual a: {area}")


principal()



    