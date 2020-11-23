from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from pg_db import acc_db as acc
import numpy as np
import pandas as pd

connection = acc.exec_con()
cabecalho = ['nest_id','treatment','r_time', 'a_x', 'a_y', 'a_z']
df = pd.read_sql_query("select a_x, a_y, a_z from data_vibration_1 where nest_id = 'N15YCC2017' and treatment = 'T02' order by r_time", connection)
population = []
for rows in df.itertuples():
    population.append([rows.a_y,rows.a_x])
X = np.array(population)

kmeans = KMeans(n_clusters = 10, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 300) #numero máximo de iterações
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,1], X[:,0], c = pred_y) #posicionamento dos eixos x e y
plt.xlim(min(X[:,1]),max(X[:,1])) #range do eixo x
plt.ylim(min(X[:,0]),max(X[:,0])) #range do eixo y
plt.grid() #função que desenha a grade no nosso gráfico
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 70, c = 'red') #posição de cada centroide no gráfico

print("KMeans - Scikit-Learn")
print("Labels")
print(kmeans.labels_)
print("Cluster centers:")
print(kmeans.cluster_centers_)

plt.show()