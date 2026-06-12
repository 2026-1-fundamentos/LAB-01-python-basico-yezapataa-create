"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    conteo_claves = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            columnas = linea.split()
            if len(columnas) >= 5:
                elementos = columnas[4].split(",")
                
                for elemento in elementos:
                    clave = elemento.split(":")[0]
                    
                    if clave in conteo_claves:
                        conteo_claves[clave] += 1
                    else:
                        conteo_claves[clave] = 1

    resultado_ordenado = {}
    for clave in sorted(conteo_claves.keys()):
        resultado_ordenado[clave] = conteo_claves[clave]

    return resultado_ordenado


if __name__ == "__main__":
    print(pregunta_09())
