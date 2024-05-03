#Ejercicio 6: Validación de Contraseña 
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.



import re

def validar_contrasena(contraseña):

    if len(contraseña) < 8:
        return False
    #verificar caracteres, mayusculas y minusculas

    if not re.search("[A-Z]", contraseña):
        return False
    if not re.search("[a-z]", contraseña):
        return False
    if not re.search("\d", contraseña):
        return False
    if not re.search("['#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']", contraseña):
        return False
    
    return True

def main():

    contraseña = input("Ingresa tu contraseña: ")

    if validar_contrasena(contraseña):
        print("La contraseña es válida.")
    else:
        print("La contraseña no cumple con los requisitos.")
        return main()

if __name__ == "__main__":
    main()

