"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo_letras = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            columnas = linea.split()
            if columnas:
                letra = columnas[0]  # La primera columna está en el índice 0
                
                if letra in conteo_letras:
                    conteo_letras[letra] += 1
                else:
                    conteo_letras[letra] = 1

    resultado_ordenado = sorted(conteo_letras.items())

    return resultado_ordenado

if __name__ == "__main__":
    print(pregunta_02())