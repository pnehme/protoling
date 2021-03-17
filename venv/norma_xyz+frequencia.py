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
    passo = passo / 10
    for i in range(10):
        if minimo + passo * i <= x < minimo + passo * (i + 1):
            valor = (i + 1) / 10
    return valor

def comparaValor(atual, anterior):
    valor = 0
    if atual > anterior:
        valor = 1
    elif atual == anterior:
        valor = 0
    else:
        valor = -1
    return valor


connection = acc.exec_con()

file = open("c:/BASE1/NNTW/amplitude-"
            "frequencia_vetores.csv", "w")
linha = ""
for i in range(1, 16):
    if i < 10:
        ninho = 'N0' + str(i) + 'YCC2017'
    else:
        ninho = 'N' + str(i) + 'YCC2017'
    for j in range(1, 5):
        tratamento = 'T0' + str(j)
        df = pd.read_sql_query(
            "select a_x, a_y, a_z, r_time from "
            "data_vibration_1 where r_time > 30 and nest_id = '" +
            ninho + "' and treatment = '" + tratamento +
            "' order by r_time limit 40000",
            connection)
        population = []
        for rows in df.itertuples():
            population.append([mt.sqrt(rows.a_x ** 2 +
                                       rows.a_y ** 2 + rows.a_z ** 2),
                                       [rows.r_time])
        X = np.array(population)
        media = X[:, 0].mean()
        sigma = X[:, 0].std()
        minimo = X[:, 0].min()
        maximo = X[:, 0].max()
        i = 1
        while (len(population) - i >= 512):
            if population[i][0] > media + 3 * sigma:
#cálculo padrão amplitude
                norma_vetor_cat = []
                freq = []
                for k in range(512):
                    norma_vetor_cat.append(comparaAmplitude(population[k + i][0],
                                                            minimo, maximo))
                    freq.append(population[k + i][0])
# cálculo de frequencia
                teste_ida = []
                teste_volta = []
                frequencia = 0
                valAnt = 0
                for j in range(len(freq)):
                    teste_ida.append(comparaValor(freq[j], valAnt))
                    valAnt = freq[j]
                valAnt = 0
                for j in range(len(freq)):
                    teste_volta.append(comparaValor(freq[len(freq)-(j + 1)], valAnt))
                    valAnt = freq[len(freq)-(j + 1)]
                for j in range(len(freq)):
                    if teste_ida[j] + teste_volta[j] == 2:
                        frequencia += 1
                AmpMedia = np.array(norma_vetor_cat).mean()
                linha += ninho+","+tratamento+","+str(i)+","+\
                         str(format(AmpMedia, '.2f'))+","+\
                         str(format(frequencia, '.2f'))+"\n"
                file.write(linha)
                linha = ""
                i += 512
            i += 1
file.close()
