from matplotlib import pyplot as plt
import math as mt
from pg_db import acc_db as acc
import numpy as np
import pandas as pd
import csv
connection = acc.exec_con()
cabecalho = ['nest_id','treatment','r_time','a_x','a_y','a_z']
for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)+'YCC2017'
    else:
        ninho = 'N'+str(i)+'YCC2017'
    for j in range(1,5):
        tratamento = 'T0'+str(j)
        df = pd.read_sql_query("select a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '"+ninho+"' and treatment = '"+tratamento+"' order by r_time", connection)
        population = []
        for rows in df.itertuples():
            population.append([mt.sqrt(rows.a_x**2 + rows.a_y**2 + rows.a_z**2),rows.r_time])
        X = np.array(population)
        media = X[:,0].mean()
        sigma = X[:,0].std()
#        minimo = X[:,0].min()
#        maximo = X[:,0].max()
#        print(ninho, tratamento, format(media, '.2f'), format(sigma,'.2f'), format(minimo, '.2f'), format(maximo, '.2f'))

        dados = ""
        passo = 1
        for i in range(len(population)):
            if population[i][0] > media + 10*sigma:
                if len(population) - i >= 512:
                    for k in range(513):
                        dados += str(format(population[k+i][0], ".2f"))+";"+str(population[k+i][1])+"\n"
                    i += 512
                    file = open("c:/BASE1/NNTW/norma_" + ninho + "-" + tratamento + "-" + str(passo) + ".txt", "w")
                    file.write(dados)
                    file.close()
                    dados = ""
                    passo += 1
                    print(ninho, tratamento, str(passo))
#        X_3sigma = np.array(dados)
#        plt.xlabel('tempo(segundos)')
#        plt.ylabel('norma(x,y,z) > 3sigma')
#        plt.plot(X_3sigma[:,1], X_3sigma[:,0])
#        plt.show()
