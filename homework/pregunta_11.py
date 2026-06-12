"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            columnas = linea.split()
            if len(columnas) >= 4:
                valor = int(columnas[1])
                
                letras_col_4 = columnas[3].split(",")
                
                for letra in letras_col_4:
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += valor
                    else:
                        suma_por_letra[letra] = valor

    resultado_ordenado = {}
    for letra in sorted(suma_por_letra.keys()):
        resultado_ordenado[letra] = suma_por_letra[letra]

    return resultado_ordenado


if __name__ == "__main__":
    print(pregunta_11())