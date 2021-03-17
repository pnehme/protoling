from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

population = pd.read_csv('c:/BASE1/NNTW/'
                         'amplitude-frequencia_vetores.csv')
pop1 = population.iloc[0:1070,3:5].copy()
print(pop1)
X = np.array(pop1)
kmeans = KMeans(n_clusters = 2,
init = 'k-means++', n_init = 100,
max_iter = 300)
pred_y = kmeans.fit_predict(X)
plt.title('Amplitude x Frequência - '+
          str(kmeans.n_clusters)+' Clusters')
plt.xlabel('frequência')
plt.ylabel('amplitude (faixa 0 a 1)')
plt.scatter(X[:,1], X[:,0], c = pred_y)
plt.xlim(min(X[:,1]),max(X[:,1]))
plt.ylim(min(X[:,0]),max(X[:,0]))
plt.grid()
plt.scatter(kmeans.cluster_centers_[:,1],
            kmeans.cluster_centers_[:,0], s = 70, c = 'red')

print("KMeans - Scikit-Learn")
print("Labels")
for i in kmeans.labels_:
    print(i)
print("Cluster centers:")
print(kmeans.cluster_centers_)

plt.show()