def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("--------------------------------------------")
    print("Opcion 1: Convertir de Celsius a Fahrenheit")
    print("Opcion 2: Convertir de Fahrenheit a Celsius")
    print("--------------------------------------------")
    opcion = input("Seleccione una opción 1 o 2: ")

    if opcion == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print("La conversion de:", celsius, "grados Celsius es igual a:", fahrenheit,"grados Fahrenheit" )
    elif opcion == '2':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"La conversion de:", fahrenheit, "grados fahrenheit es igual a:", celsius,"grados Celsius" )
    else:
        print("*************************************")
        print("Opción no válida. Seleccione 1 o 2.")
        print("*************************************")
        return main()
if __name__ == "__main__":
    main()
