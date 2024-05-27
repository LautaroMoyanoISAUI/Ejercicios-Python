#Desarrolla un programa en Python que convierta una 
#cantidad de dinero de dólares estadounidenses a euros. 
#El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar 
#la cantidad equivalente en euros, utilizando un tipo de cambio fijo.

print("CONVERSOR DE DOLAR A EURO (VALOR DOLAR 1 = EURO 0.93)")

dolares = float(input("Ingrese la cantidad de dolares a convertir: "))
euro = 0.93478
cambio = dolares * euro

print("Usted convirtio", dolares, "Dolares a", cambio, "Euros")


