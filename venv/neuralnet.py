from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from pg_db import acc_db as acc
import numpy as np
import pandas as pd

connection = acc.exec_con()
cabecalho = ['nest_id','treatment','r_time', 'a_x', 'a_y', 'a_z']
df = pd.read_sql_query("select a_x, a_y, a_z from data_vibration where nest_id = 'N01YCC2017-V01' and treatment = 'T02' order by r_time", connection)


population = []
for rows in df.itertuples():
    population.append([rows.a_y,rows.a_z])
print(population)
# Cores a serem utilizadas pelo Matplotlib para apresentar os dados.
colors = [
    "#FF0000",
    "#00FF00",
    "#0000FF",
    "#FF00FF",
    "#FFFF00",
    "#00FFFF",
    "#220000",
    "#002200",
    "#000022",
    "#220022",
    "#222200",
    "#002222",
    "#550000",
    "#005500",
    "#800000",
    "#008000",
    "#000080",
    "#800080",
    "#808000",
    "#800080",
]

color_names = {"#FF0000": "vermelho", "#00FF00": "verde", "#0000FF": "azul"}

plt.title("Distribuicao dos dados da coleta")
plt.xlabel("eixo Y")
plt.ylabel("eixo Z")
print(len(population))
for i in range(0, len(population)):
    plt.scatter(population[i][0], population[i][1], color="green")

X = np.array(population)

# Executa k-means sobre os pontos onde as pessoas est�o concentradas,
# simulacao com k = 3.
kmeans = KMeans(n_clusters=20, random_state=0).fit(X)
print("KMeans - Scikit-Learn")
print("Labels")
print(kmeans.labels_)
print("Cluster centers:")
print(kmeans.cluster_centers_)

for i in range(0, len(kmeans.cluster_centers_)):
    color_idx = i
    plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1], color=colors[color_idx], marker="+",
                s=100)
plt.show()

# Tenta prever a qual cluster pertence determinada pessoa dada sua localiza��o.
#osasco_person = [[40, 120]]
#cluster_id = kmeans.predict(osasco_person)
#print("Morador de Osasco deve ir para hospital: %s" % cluster_id)
#print("Cor: %s" % color_names[colors[int(cluster_id)]])