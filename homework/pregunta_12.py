"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            columnas = linea.split()
            if len(columnas) >= 5:
                letra_clave = columnas[0]
                
                elementos = columnas[4].split(",")
                suma_linea = 0
                for elemento in elementos:
                    valor = int(elemento.split(":")[1])
                    suma_linea += valor
                
                if letra_clave in suma_por_letra:
                    suma_por_letra[letra_clave] += suma_linea
                else:
                    suma_por_letra[letra_clave] = suma_linea

    resultado_ordenado = {}
    for letra in sorted(suma_por_letra.keys()):
        resultado_ordenado[letra] = suma_por_letra[letra]

    return resultado_ordenado


if __name__ == "__main__":
    print(pregunta_12())