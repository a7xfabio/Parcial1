#/usr/bin/python3

import math 
import numpy as np

calificaciones_finales = [7, 8, 9, 4, 5]
print(np.mean(calificaciones_finales))

curva_calificaciones_finales = [math.sqrt(calificaciones_finales) * 10 
for nota in calificaciones_finales]
print(np.mean(curva_calificaciones_finales))