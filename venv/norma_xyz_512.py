import math as mt
from pg_db import acc_db as acc
import numpy as np
import pandas as pd
import csv

connection = acc.exec_con()
dados = ""
padrao = ""
file = open("c:/BASE1/NNTW/norma_xyz_512.csv", "w")
cabecalho = "ninho,trat,time,"
for campo in range(1,512):
    cabecalho += str(campo)+','
cabecalho += "512\n"
file.write(cabecalho)
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
        i = 1
        while (len(population) - i >= 512):
            if population[i][0] > media + 3 * sigma:
                dados = ""
                for k in range(512):
                    norma_vetor_cat = population[k + i][0]
                    if k < 511:
                        dados += str(norma_vetor_cat) + ","
                    else:
                        dados += str(norma_vetor_cat) + "\n"
                file.write(ninho+","+tratamento+","+str(population[i][1])+","+dados)
                print(ninho+","+tratamento+","+str(population[i][1]))
                i += 512
            i += 1
file.close()
