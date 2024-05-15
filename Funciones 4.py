"""Ejercicio 4
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
3 oportunidades."""


def login(nombre_usuario, contraseña):

    if nombre_usuario == 'usuario1' and contraseña == 'asdasd':
        return True
    return False

def validar_intentos(intento):

    if intento < 3:
        return True
    return False

def principal():
    intento = 0
    
    while validar_intentos(intento):
        nombre_usuario = input("Ingrese nombre de Usuario: ")
        contraseña = input("Ingrese contraseña: ")

        if login(nombre_usuario, contraseña):
            print("Has iniciado sesion!")

        else:
            intento += 1
            intentos_restantes = 3 -intento
            if intentos_restantes > 0:

                print(f"Usuario o contraseña incorrecto! te quedan {intentos_restantes} intentos.")
            else:
                print("Ingreso Denegado")
                break
principal()


    







