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

target = np.identity(59,dtype=float)
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
        file = open("c:/BASE1/NNTW/normas"+ninho+"-"+tratamento+".csv", "w")
        dados = 'norma_vetor,r_time\n'
        X = np.array(population)
        for i in range(len(population)):
            dados += str(format(population[i][0], '.2f')) + ',' + str(population[i][1])+ '\n'
        print(ninho, tratamento)
        file.write(dados)
        file.close()
        dados = ''

