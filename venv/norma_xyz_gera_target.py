from matplotlib import pyplot as plt
import math as mt
from pg_db import acc_db as acc
import numpy as np
import pandas as pd
import csv

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
target = np.identity(59,dtype=float)
dados = ''
indice = -1
file = open("c:/BASE1/NNTW/norma_padroes_fit.csv", "w")
'''
cabecalho = ''
for i in range(1,513):
    cabecalho += str(i)+','
for i in range(1001,1060):
    if i < 1059:
        cabecalho += str(i) + ','
    else:
        cabecalho += str(i) + '\n'
file.write(cabecalho)
'''
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
        media = X[:,0].mean()
        sigma = X[:,0].std()
        minimo = X[:,0].min()
        maximo = X[:,0].max()
        passo = 0
        for i in range(len(population)):
            if population[i][0] > media + 4 * sigma:
                if len(population) - i >= 512:
                    for k in range(1,513):
                        dados += str(comparaAmplitude(population[k+i][0], minimo, maximo)) + "," 
                    for id in range(0,59):
                        if id < 58:
                            dados += str(target[indice][id]) + ','
                        else:
                            dados += str(target[indice][id]) + '\n'
                    i += 512
                    file.write(dados)
                    dados = ""
                    passo += 1
                    print(ninho, tratamento, str(passo))
                if passo == 3:
                    passo = 0
                    break
file.close()


