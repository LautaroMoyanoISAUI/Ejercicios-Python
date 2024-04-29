#Escribe un programa en Python que solicite al usuario que ingrese la base y la altura de un triángulo,
# y luego calcule y muestre el área del triángulo.

print("CALCULADOR AREA DE UN TRIANGULO")

altura = float(input("Ingrese la altura del triangulo: "))
base = float(input("Ingrese la base del triangulo: "))

area = (altura * base) / 2

print("El area de el trianguro es igual a: ", area)