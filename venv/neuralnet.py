from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from pg_db import acc_db as acc
import numpy as np
import pandas as pd
target = np.identity(60,dtype=float)
entrada = []
indice = 0
for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)
    else:
        ninho = 'N'+str(i)
    for j in range(1,5):
        tratamento = 'T0'+str(j)
        arquivo = open('/BASE1/NNTW/norma_'+ninho+'YCC2017-'+tratamento+'-1.txt', 'r')
        lista = arquivo.read()
        lista = lista.replace('\n', ';')
        dados = lista.split(';')
#        print(dados)
        lista = []
        i = 0
        for x in dados:
            i += 1
            if i % 2 != 0:
                if x != '':
                    lista.append(x)
        a = np.array(lista, dtype=float)
        entrada.append([a,target[indice]])
        indice += 1
        arquivo.close()

redeneural = MLPClassifier(verbose=True,
                           max_iter=1000,
                           tol=0.00001,
                           activation='logistic',
                           learning_rate_init=0.001)
redeneural.fit(entrada[0,:],entrada[:,1])
'''
connection = acc.exec_con()
cabecalho = ['nest_id','treatment','r_time', 'a_x', 'a_y', 'a_z']
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



df = pd.read_sql_query("select a_x, a_y, a_z from data_vibration where nest_id = 'N01YCC2017-V01' and treatment = 'T02' order by r_time", connection)
population = []
for rows in df.itertuples():
    population.append([rows.a_x,rows.a_z])
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
plt.xlabel("eixo X")
plt.ylabel("eixo Z")
print(len(population))
for i in range(0, len(population)):
    plt.scatter(population[i][0], population[i][1], color="green")

X = np.array(population)
kmeans = KMeans(n_clusters=10, init ='k-means++', max_iter=300, n_init=10, random_state=0).fit(X)

#plot variance for each value for 'k' between 1,10

# Executa k-means sobre os pontos onde as pessoas est�o concentradas,
# simulacao com k = 3.
#kmeans = KMeans(n_clusters=10, init ='k-means++', max_iter=300, n_init=10, random_state=0).fit(X)
print("KMeans - Scikit-Learn")
print("Labels")
print(kmeans.labels_)
print("Cluster centers:")
print(kmeans.cluster_centers_)

for i in range(0, len(kmeans.cluster_centers_)):
    color_idx = i
    plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1], color=colors[color_idx],
                s=100)

plt.show()

# Tenta prever a qual cluster pertence determinada pessoa dada sua localiza��o.
#osasco_person = [[40, 120]]
#cluster_id = kmeans.predict(osasco_person)
#print("Morador de Osasco deve ir para hospital: %s" % cluster_id)
#print("Cor: %s" % color_names[colors[int(cluster_id)]])
'''