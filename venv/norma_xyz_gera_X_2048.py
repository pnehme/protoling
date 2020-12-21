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
file = open("c:/BASE1/NNTW/norma_padroes_2048.csv", "w")

for i in range(1, 16):
    if i < 10:
        ninho = 'N0' + str(i) + 'YCC2017'
    else:
        ninho = 'N' + str(i) + 'YCC2017'
    for j in range(1, 5):
        tratamento = 'T0' + str(j)
        df = pd.read_sql_query(
            "select a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '" + ninho + "' and treatment = '" + tratamento + "' order by r_time",
            connection)
        population = []
        for rows in df.itertuples():
            population.append([mt.sqrt(rows.a_x ** 2 + rows.a_y ** 2 + rows.a_z ** 2), rows.r_time])
        X = np.array(population)
        media = X[:, 0].mean()
        sigma = X[:, 0].std()
        minimo = X[:, 0].min()
        maximo = X[:, 0].max()
        i = 1
        while (len(population) - i >= 2048):
            if population[i][0] > media + 3 * sigma:
                dados = ""
                freq = []
                teste_ida = []
                teste_volta = []
                frequencia = 0
                for k in range(2048):
                    norma_vetor_cat = comparaAmplitude(population[k + i][0], minimo, maximo)
                    if k < 2047:
                        dados += str(norma_vetor_cat) + ","
                    else:
                        dados += str(norma_vetor_cat) + "\n"
                file.write(dados)
                print(ninho+"-"+tratamento+"-"+str(i))
                i += 2048
            i += 1
file.close()
