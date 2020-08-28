import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

calculo = [df.alcohol.median(),df.pH.median(),df.residual_sugar.median(),
df.citric_acid.median()]

def medi(mediana_valor, columna_valor):
    for i, valor in enumerate(columna_valor):
        if valor >= mediana_valor:
            df.loc[i, valor] = 'alto'
        else:
            df.loc[i, valor] = 'bajo'
    calculo = df.groupby(valor).quality.mean()
    return print(calculo)


Alcohol = medi(calculo[0], df.alcohol)
PH = medi(calculo[1], df.pH)
RS = medi(calculo[2], df.residual_sugar)
AC = medi(calculo[3], df.citric_acid)

