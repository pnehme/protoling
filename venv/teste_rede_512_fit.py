from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import csv
import pickle


norma = pd.read_csv('c:/BASE1/NNTW/norma_padroes_512_fit.csv')
entradas = norma.iloc[1:600,0:512].copy()
saidas = norma.iloc[1:600,512:514].copy()
#print(entradas)

redeneural = MLPClassifier(verbose=True,
                           max_iter=100000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.00001)


redeneural.fit(entradas,saidas)


filename = 'c:/BASE1/NNTW/modelo_final512.pkl'
with open(filename, 'wb') as file:
    pickle.dump(redeneural, file)

