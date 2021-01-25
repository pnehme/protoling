from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from pg_db import acc_db as acc
import numpy as np
import pandas as pd

population = pd.read_csv('c:/BASE1/NNTW/parametros.csv')
X = np.array(population)
kmeans = KMeans(n_clusters = 20, #numero de clusters
init = 'k-means++', n_init = 20, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 300) #numero máximo de iterações
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,1], X[:,0], c = pred_y) #posicionamento dos eixos x e y
plt.xlim(min(X[:,1]),max(X[:,1])) #range do eixo x
plt.ylim(min(X[:,0]),max(X[:,0])) #range do eixo y
plt.grid() #função que desenha a grade no nosso gráfico
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 70, c = 'red') #posição de cada centroide no gráfico

print("KMeans - Scikit-Learn")
print("Labels")
for i in kmeans.labels_:
    print(i)
print("Cluster centers:")
print(kmeans.cluster_centers_)

plt.show()