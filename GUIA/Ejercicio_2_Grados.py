#Solicita al usuario que ingrese una temperatura en grados Celsius.
#Convierte la temperatura ingresada a grados Fahrenheit utilizando la fórmula proporcionada.
#Muestra el resultado al usuario.

Celsius = int(input("Ingrese la temperatura en Grados Celsius que desee convertir: "))

Fahrenheit = (Celsius * (9/5)) + 32

print("Su temperatura en grados Fahrenheit es: ", Fahrenheit)
