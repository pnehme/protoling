from matplotlib import pyplot as plt
import math as mt
from pg_db import acc_db as acc
import numpy as np
import pandas as pd

indice = -1
connection = acc.exec_con()
ninho = 'N13YCC2017'
tratamento = 'T01'
faixa = '43 and 44 '
df = pd.read_sql_query("select a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '"+ninho+"' and treatment = '"+tratamento+"' and r_time between "+faixa+" order by r_time", connection)
population = []
for rows in df.itertuples():
    population.append([mt.sqrt(rows.a_x**2 + rows.a_y**2 + rows.a_z**2),rows.r_time])
X_3sigma = np.array(population)
plt.clf()
plt.title(ninho+"-"+tratamento)
plt.xlabel('tempo(acelerômetro)')
plt.ylabel('norma(x,y,z)')

plt.plot(X_3sigma[:,1], X_3sigma[:,0])

plt.show()
#plt.savefig("C:/Ciencia_dados_PUC/Redes neurais/analise_protoling/normas_vetores/detalhamento/"+ninho+"-"+tratamento+"-"+faixa+".jpg")



