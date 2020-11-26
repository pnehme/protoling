from sklearn.neural_network import MLPClassifier
#from sklearn import datasets
import pandas as pd
#import numpy as np
import csv
'''
data = {}
with open("c:/BASE1/NNTW/norma.csv") as arquivocsv:
    ler = csv.DictReader(arquivocsv, delimiter=",")
    for linhas in ler:
        print(linhas)


vals = np.fromiter(ler.values(), dtype=float)
print(vals)
'''
norma = pd.read_csv('c:/BASE1/NNTW/norma_cluster_faixas.csv')
entradas = norma.iloc[0:171,0:510].copy()
saidas = norma.iloc[0:171,511:570].copy()


redeneural = MLPClassifier(verbose=True,
                           max_iter=100000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeneural.n_outputs_= 59
redeneural.fit(entradas,saidas)
