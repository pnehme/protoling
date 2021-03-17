from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import csv
import pickle


result = open("c:/BASE1/NNTW/resultado_rede512_teste.csv",'w')
writer = csv.writer(result, delimiter=",", lineterminator="\n", dialect = 'excel')

filename = 'c:/BASE1/NNTW/modelo_final512.pkl'
with open(filename, 'rb') as file:
    modelo_carregado = pickle.load(file)

base = pd.read_csv('c:/BASE1/NNTW/norma_padroes_512_fit.csv')
X = base.iloc[1:1070,0:512].copy()
#counter = 1
for line in modelo_carregado.predict(X):
    writer.writerow(line)
#    print(counter, X.iloc[0:counter,0:5].copy())
#    counter += 1
print("Concluído!")
result.close()
