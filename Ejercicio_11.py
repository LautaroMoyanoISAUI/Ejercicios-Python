


def juego_busqueda_binaria():

    numero_min = 1
    numero_max = 100
    intento = 0

    while True:
        intento_programa = (numero_min + numero_max) // 2
        intento += 1

        print(f"Es {intento_programa} tu numero?")
        respuesta = (input("Ingrese menor, mayor o igual: ")).lower()

        if respuesta == "igual":
            print(f"Adivine en {intento} intentos!! Gracias por jugar!! <3")
            break
        elif respuesta == "mayor":
            numero_min = intento_programa + 1
        elif respuesta == "menor":
            numero_max = intento_programa - 1
        else:
            print("Respuesta no valida, porfavor escribe mayor, menor o igual")

juego_busqueda_binaria()

        



