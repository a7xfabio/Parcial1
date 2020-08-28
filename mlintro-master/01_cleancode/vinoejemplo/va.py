
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

media_alcohol = df.alcohol.median()            
for count, alcohol in enumerate(df.alcohol):
    if alcohol >= media_alcohol:
        df.loc[count, 'alcohol'] = 'alto'
    else:
        df.loc[count, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

media_pH = df.pH.median()
for count, pH in enumerate(df.pH):
    if pH >= media_pH:
        df.loc[count, 'pH'] = 'alto'
    else:
        df.loc[count, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

media_sugar = df.residual_sugar.median()   #se cambio el residual sugar por residual_sugar
for count, residual_sugar in enumerate(df.residual_sugar): #cambiar el sugar por el residual_sugar
    if residual_sugar >= media_sugar:
        df.loc[count, 'residual sugar'] = 'alto'
    else:
        df.loc[count, 'residual sugar'] = 'bajo'
df.groupby('residual sugar').quality.mean()

media_citric = df.citric_acid.median()      #se cambio citric acid por citric_acid
for count, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= media_citric:
        df.loc[count, 'citric acid'] = 'alto'
    else:
        df.loc[count, 'citric acid'] = 'bajo'
df.groupby('citric acid').quality.mean()