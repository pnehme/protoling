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
entradas = norma.iloc[0:73,0:2047].copy()
saidas = norma.iloc[0:73,2048:2053].copy()

redeneural = MLPClassifier(verbose=True,
                           max_iter=10000,
                           tol=0.000001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeneural.n_outputs_= 6
redeneural.fit(entradas,saidas)
'''
X = pd.read_csv('c:/BASE1/NNTW/norma_padroes_2048.csv')
print(redeneural.predict(X))
'''