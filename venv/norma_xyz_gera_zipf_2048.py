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
            valor = i / 40
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
target = np.identity(6, dtype=float)
dados = ""
padrao = ""
for i in range(1, 16):
    if i < 10:
        ninho = 'N0' + str(i) + 'YCC2017'
    else:
        ninho = 'N' + str(i) + 'YCC2017'
    for j in range(1, 5):
        tratamento = 'T0' + str(j)
        file = open("c:/BASE1/NNTW/2048/norma_2048"+ninho+"-"+tratamento+".csv", "w")
        df = pd.read_sql_query(
            "select a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '" + ninho + "' and treatment = '" + tratamento + "' order by r_time",
            connection)
        population = []
        for rows in df.itertuples():
            population.append([mt.sqrt(rows.a_x ** 2 + rows.a_y ** 2 + rows.a_z ** 2), rows.r_time])
        i = 1
        tempo = ""
        bloco = 0
        X = np.array(population)
        media = X[:, 0].mean()
        sigma = X[:, 0].std()
        while (len(population) - i >= 2048):
            if population[i][0] > media + 3 * sigma:
                dados = ""
                bloco += 1
                tempo = str(population[i][1])
                for k in range(2048):
                    if k < 2047:
                        dados += str(format(population[k + i][0],'.2f')) + ","
                    else:
                        dados += str(format(population[k + i][0],'.2f')) + "\n"
                file.write(dados)
                print(ninho+"-"+tratamento+"-bloco="+str(bloco)+"-"+tempo)
                i += 2048
            i += 1
        file.close()
