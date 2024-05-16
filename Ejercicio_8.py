#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
#La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), 
#números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.

import random
print("GENERADOR DE CONTRASEÑAS ALEATORIAS")
print("-------------------------------------")

def generar_contraseña(longitud):
    contraseña = ""
    for i in range(longitud):
        caracteres = random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890!$%&?¡")
        contraseña += caracteres
    return contraseña

longitud = int(input("Ingrese de que tamaño desea su contraseña(min 12 caracteres)"))

if longitud > 11:

    nueva_contraseña = generar_contraseña(longitud)
    print("Su nueva contraseña es: ", nueva_contraseña)
else:
    print("La contraseña debe contener 12 caracteres o mas")    

