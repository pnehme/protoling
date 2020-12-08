from matplotlib import pyplot as plt
import math as mt
from pg_db import acc_db as acc
import numpy as np
import pandas as pd

def comparaAmplitude(x, minimo, maximo):
    valor = 0
    passo = 0
    passo = maximo - minimo
    passo = passo / 40
    for i in range(40):
        if minimo + passo * i <= x < minimo + passo * (i + 1):
           valor = i/40
    return valor

indice = -1
connection = acc.exec_con()
for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)+'YCC2017'
    else:
        ninho = 'N'+str(i)+'YCC2017'
    for j in range(1,5):
        indice += 1
        tratamento = 'T0'+str(j)
        df = pd.read_sql_query("select a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '"+ninho+"' and treatment = '"+tratamento+"' order by r_time", connection)
        population = []
        for rows in df.itertuples():
            population.append([mt.sqrt(rows.a_x**2 + rows.a_y**2 + rows.a_z**2),rows.r_time])
        X = np.array(population)
        media = X[:, 0].mean()
        sigma = X[:, 0].std()
        minimo = X[:, 0].min()
        maximo = X[:, 0].max()
        population3s = []
        for i in range(len(population)):
            if population[i][0] > media + 4 * sigma:
                population3s.append([population[i][0],population[i][1]])
            else:
                population3s.append([media,population[i][1]])
        X_3sigma = np.array(population3s)
        plt.clf()
        plt.title(ninho+"-"+tratamento)
        plt.xlabel('tempo(acelerômetro)')
        plt.ylabel('norma(x,y,z)')
        plt.plot(X_3sigma[:,1], X_3sigma[:,0])
#        plt.show()
        plt.savefig("C:/Ciencia_dados_PUC/Redes neurais/analise_protoling/normas_vetores/detalhamento/"+ninho+"-"+tratamento+".jpg")



