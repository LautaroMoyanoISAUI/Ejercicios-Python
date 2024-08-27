"""Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes y
 los valores son listas de sus calificaciones. La función debe devolver un nuevo diccionario con las mismas claves pero donde 
 los valores son la calificación promedio de cada estudiante.
"""

def nota_estudiantes(diccionario_estudiantes):
    promedios = {}
    for estudiante, notas in diccionario_estudiantes.items():
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio
    return promedios

#promedios[estudiante] = promedio le das un valor a estudiante 
#promedios[estudiante] = [promedio] cambias
diccionario_estudiantes = {
    "Lautaro": [9, 10, 8],
    "Agus": [10, 8, 8],
    "Silvana": [7, 10, 6]

}

resultado = nota_estudiantes(diccionario_estudiantes)
print(resultado)