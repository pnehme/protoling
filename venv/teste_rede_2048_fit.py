from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import csv
import pickle


norma = pd.read_csv('c:/BASE1/NNTW/norma_padroes_2048_fit.csv')
entradas = norma.iloc[0:73,0:2048].copy()
saidas = norma.iloc[0:73,2048:2054].copy()

redeneural = MLPClassifier(verbose=True,
                           max_iter=10000,
                           tol=0.000001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeneural.n_outputs_= 6
redeneural.fit(entradas,saidas)


filename = 'c:/BASE1/NNTW/modelo_final.pkl'
with open(filename, 'wb') as file:
    pickle.dump(redeneural, file)

