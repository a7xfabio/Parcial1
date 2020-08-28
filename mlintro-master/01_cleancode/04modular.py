import math
import numpy as np

resultados_pruebas = [88, 92, 79, 93, 85]
print(np.mean(resultados_pruebas))

curva_5 = [resultado + 5 for resultado in resultados_pruebas]
print(np.mean(curva_5))

curva_10 = [resultado + 10 for resultado in resultados_pruebas]
print(np.mean(curva_10))
