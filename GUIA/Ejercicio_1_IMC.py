#Solicita al usuario que ingrese su peso en kilogramos.
#Solicita al usuario que ingrese su altura en metros.
#Calcula el IMC utilizando la fórmula proporcionada.
#Muestra el resultado al usuario.

peso = float(input("Ingrese su peso en Kilogramos(Kg): "))
altura = float(input("Ingrese su Altura en metros: "))

IMC = peso / (altura * altura)

print("Su IMC es igual a: ", IMC)