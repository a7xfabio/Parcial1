#/usr/bin/python3

n = [7, 8, 9, 4, 5] #notas finales del grupo de SE
print(sum(n)/len(n)) #calcula y muestra la media de las calificaicones

n1 = [x ** 0.5 * 10 for x in n] #curva de las calificaciones usando el metodo de raiz elevada a la decima potencia y se almacena en un lista
print(sum(n1)/len(n1)) #calcula y muestra la media de la curva de las calificaicones
