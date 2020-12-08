from sklearn.neural_network import MLPClassifier
from pg_db import acc_db as acc
import math as mt
import pandas as pd
import numpy as np
import csv
import pickle

def comparaAmplitude(x, minimo, maximo):
    valor = 0
    passo = 0
    passo = maximo - minimo
    passo = passo / 40
    for i in range(40):
        if minimo + passo * i <= x < minimo + passo * (i + 1):
           valor = i/40
    return valor

connection = acc.exec_con()

norma = pd.read_csv('c:/BASE1/NNTW/norma_padroes_2048_fit.csv')
entradas = norma.iloc[0:171,0:2047].copy()
saidas = norma.iloc[0:171,2048:2053].copy()

redeneural = MLPClassifier(verbose=True,
                           max_iter=100000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeneural.n_outputs_= 6
redeneural.fit(entradas,saidas)
'''
meu_arquivo = open('c:/BASE1/NNTW/weigths.p', 'wb')

pickle.dump(redeneural, meu_arquivo)
meu_arquivo.close()

meu_arquivo = open('c:/BASE1/NNTW/weights.p',  'rb')
redeneural = pickle.load(meu_arquivo)
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
dados = []
for n in range(len(population)):
    dados.append(comparaAmplitude(population[n], minimo, maximo))
    i = i+1
    if i == 511:
        X = np.array(dados).reshape(1,-1)
        S = redeneural.predict_log_proba(X)
        print(S)
        dados = []
        i = 0
'''
