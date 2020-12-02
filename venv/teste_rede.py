from sklearn.neural_network import MLPClassifier
import math as mt
import pandas as pd
from pg_db import acc_db as acc
import csv

def comparaAmplitude(x, minimo, maximo):
    valor = 0
    passo = 0
    passo = maximo - minimo
    passo = passo / 40
    for i in range(1,41):
        if minimo + passo * (i - 1) <= x < minimo + passo * i:
           valor = i/40
    return valor

connection = acc.exec_con()

norma = pd.read_csv('c:/BASE1/NNTW/norma_cluster_faixas.csv')
entradas = norma.iloc[0:171,0:510].copy()
saidas = norma.iloc[0:171,511:570].copy()

redeneural = MLPClassifier(verbose=False,
                           max_iter=100000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeneural.n_outputs_= 59
redeneural.fit(entradas,saidas)
ninho = 'N01YCC2017'
tratamento = 'T01'
df = pd.read_sql_query(
    "select a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '" + ninho + "' and treatment = '" + tratamento + "' order by r_time",
    connection)
population = []
i = 0
for rows in df.itertuples():
    population.append(mt.sqrt(rows.a_x ** 2 + rows.a_y ** 2 + rows.a_z ** 2))
minimo = min(population)
maximo = max(population)

for n in range(len(population)):
    population[n] = comparaAmplitude(population[n], minimo, maximo)

X

