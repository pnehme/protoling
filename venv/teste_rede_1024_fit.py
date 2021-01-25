from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import csv
import pickle


norma = pd.read_csv('c:/BASE1/NNTW/norma_padroes_1024_fit.csv')
entradas = norma.iloc[0:793,0:1024].copy()
saidas = norma.iloc[0:793,1024:1035].copy()
print(saidas)

redeneural = MLPClassifier(verbose=True,
                           max_iter=100000,
                           tol=0.0001,
                           activation='identity',
                           learning_rate_init=0.00001)


redeneural.fit(entradas,saidas)


filename = 'c:/BASE1/NNTW/modelo_final1024.pkl'
with open(filename, 'wb') as file:
    pickle.dump(redeneural, file)

