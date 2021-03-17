from matplotlib import pyplot as plt
import math as mt
from pg_db import acc_db as acc
import numpy as np
import pandas as pd

connection = acc.exec_con()

for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)+'YCC2017'
    else:
        ninho = 'N'+str(i)+'YCC2017'
    for j in range(1,5):
        tratamento = 'T0'+str(j)
        df = pd.read_sql_query("select a_x, a_y, a_z, r_time "
                               "from data_vibration_1 where nest_id = '"+
                               ninho+"' and treatment = '"+tratamento+
                               "' order by r_time", connection)
        population = []
        for rows in df.itertuples():
            population.append([mt.sqrt(rows.a_x**2 + rows.a_y**2 +
                                       rows.a_z**2),rows.r_time])
        norma_xyz = np.array(population)
        plt.clf()
        plt.title(ninho+"-"+tratamento)
        plt.xlabel('tempo(acelerômetro)')
        plt.ylabel('norma(x,y,z)')
        plt.plot(norma_xyz[:,1], norma_xyz[:,0])
        plt.savefig("C:/Ciencia_dados_PUC/Redes neurais/"
                    "analise_protoling/normas_vetores/"+ninho+"-"+
                    tratamento+".jpg")

#file.close()

