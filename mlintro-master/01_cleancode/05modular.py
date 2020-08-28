import math
import numpy as np

def curva_plana(arreglo, n):
    return [i +n for i in arreglo]

def curva_raiz_cuadrada(arreglo):
    return [math.sqrt(i) * 10 for i in arreglo]

resultados_pruebas = [88, 92, 79, 93, 85]
curva_5 = curva_plana(resultados_pruebas, 5)
curva_10 = curva_plana(resultados_pruebas, 10)
curva_2 = curva_raiz_cuadrada(resultados_pruebas)

for listado_resultados in resultados_pruebas, curva_5, curva_10, curva_2:
    print(np.mean(listado_resultados))
