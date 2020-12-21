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
            valor = (i + 1) / 40
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
dados = ""
padrao = ""
file = open("c:/BASE1/NNTW/norma_padroes_2048_fit.csv", "w")

for i in range(1, 16):
    if i < 10:
        ninho = 'N0' + str(i) + 'YCC2017'
    else:
        ninho = 'N' + str(i) + 'YCC2017'
    for j in range(1, 5):
        tratamento = 'T0' + str(j)
        df = pd.read_sql_query(
            "select a_x, a_y, a_z, r_time from data_vibration_1 where r_time > 30 and nest_id = '" + ninho + "' and treatment = '" + tratamento + "' order by r_time limit 20000",
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
#cálculo padrão amplitude
                padrao = ""
                if population[i][0]/maximo < 0.94:
                    padrao = 'A'
                elif population[i][0]/maximo < 0.97:
                    padrao = 'B'
                else:
                    padrao = 'C'
                dados = ""
                freq = []
                teste_ida = []
                teste_volta = []
                frequencia = 0
                for k in range(2048):
                    norma_vetor_cat = comparaAmplitude(population[k + i][0], minimo, maximo)
                    dados += str(norma_vetor_cat) + ","
                    freq.append(population[k + i][0])
# cálculo de frequencia
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

# definindo o padrão da frequência
                if frequencia / len(freq) < 0.25:
                    padrao += "A"
                elif frequencia / len(freq) < 0.35:
                    padrao += "B"
                else:
                    padrao += "C"
                if padrao == "AA":
                    padrao = "0,0,0,0,0,0,0,0,1\n"
                elif padrao == "AB":
                    padrao = "0,0,0,0,0,0,0,1,0\n"
                elif padrao == "AC":
                    padrao = "0,0,0,0,0,0,1,0,0\n"
                elif padrao == "BA":
                    padrao = "0,0,0,0,0,1,0,0,0\n"
                elif padrao == "BB":
                    padrao = "0,0,0,0,1,0,0,0,0\n"
                elif padrao == "BC":
                    padrao = "0,0,0,1,0,0,0,0,0\n"
                elif padrao == "CA":
                    padrao = "0,0,1,0,0,0,0,0,0\n"
                elif padrao == "CB":
                    padrao = "0,1,0,0,0,0,0,0,0\n"
                else:
                    padrao = "1,0,0,0,0,0,0,0,0\n"
                dados += padrao
                file.write(dados)
                print(ninho+"-"+tratamento+"-"+str(i)+"-"+str(norma_vetor_cat)+"-"+str(frequencia / len(freq)))
                i += 2048
            i += 1
file.close()
