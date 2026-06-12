"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            columnas = linea.split()
            if len(columnas) >= 2:
                letra = columnas[0]
                valor = int(columnas[1])
                
                if letra in valores_por_letra:
                    valores_por_letra[letra].append(valor)
                else:
                    valores_por_letra[letra] = [valor]

    resultado = []
    for letra in sorted(valores_por_letra.keys()):
        maximo = max(valores_por_letra[letra])
        minimo = min(valores_por_letra[letra])
        resultado.append((letra, maximo, minimo))

    return resultado

if __name__ == "__main__":
    print(pregunta_05())