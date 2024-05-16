#Desarrolla un programa en Python que solicite al usuario que 
#ingrese una frase y luego cuente y muestre el número de palabras en esa frase.

frase = input("Ingrese una frase: ")
palabras = frase.split()
print(len(palabras))


