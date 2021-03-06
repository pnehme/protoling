from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import csv
import pickle


result = open("c:/BASE1/NNTW/resultado_rede2048.csv",'w')
writer = csv.writer(result, delimiter=",", lineterminator="\n", dialect = 'excel')

filename = 'c:/BASE1/NNTW/modelo_final.pkl'
with open(filename, 'rb') as file:
    modelo_carregado = pickle.load(file)

X = pd.read_csv('c:/BASE1/NNTW/norma_padroes_2048.csv')
counter = 1
for line in modelo_carregado.predict(X):
    writer.writerow(line)
    print(counter, X.iloc[0:counter,0:10].copy())
    counter += 1
result.close()
