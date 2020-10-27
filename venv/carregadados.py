from pg_db import acc_db as acc
from collections import Counter as ct
import pandas as pd
#import matplotlib.pyplot as plt
import math as mt
import csv
def calcMedia(lista):
    media = 0.0
    for i in lista:
        media += i
    return (media/len(lista))

def calcDesvio(lista):
    media = calcMedia(lista)
    variancia = 0.0
    for i in lista:
        variancia += mt.pow((i-media),2)
    return (mt.sqrt(variancia/len(lista)))

def comparaValor(atual, anterior):
    valor = 0
    if atual > anterior:
        valor = 1
    elif atual == anterior:
        valor = 0
    else:
       valor = -1
    return valor

connection = acc.exec_con()
result = open("c:/BASE1/resultado_frequencias.csv",'w')
writer = csv.writer(result, delimiter=",", lineterminator="\n", dialect = 'excel')
for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)+'YCC2017'
    else:
        ninho = 'N'+str(i)+'YCC2017'
    for j in range(1,5):
        tratamento = 'T0'+str(j)
        df = pd.read_sql_query("select nest_id, treatment, a_x, a_y, a_z, r_time from data_frequency where nest_id = '"+ninho+"' and treatment = '"+tratamento+"' order by nest_id, treatment, r_time", connection)
        freqIdaX = []
        freqVoltaX = []
        freqIdaY = []
        freqVoltaY = []
        freqIdaZ = []
        freqVoltaZ = []
        valAnt = 0
        for i in df['a_x']:
            freqIdaX.append(comparaValor(i, valAnt))
            valAnt = i
        valAnt = 0
        for i in df['a_y']:
            freqIdaY.append(comparaValor(i, valAnt))
            valAnt = i
        valAnt = 0
        for i in df['a_z']:
            freqIdaZ.append(comparaValor(i, valAnt))
            valAnt = i
        df1 = df.sort_values('r_time',ascending=False)
        valAnt = 0
        for i in df1['a_x']:
            freqVoltaX.append(comparaValor(i, valAnt))
            valAnt = i
        valAnt = 0
        for i in df1['a_y']:
            freqVoltaY.append(comparaValor(i, valAnt))
            valAnt = i
        valAnt = 0
        for i in df1['a_z']:
            freqVoltaZ.append(comparaValor(i, valAnt))
            valAnt = i
        i = 0
        j = 0
        k = 0
        listaFrequenciaX = []
        listaFrequenciaY = []
        listaFrequenciaZ = []
#calcula frequencias X
        for i in range(len(freqIdaX)):
            if freqIdaX[i] == freqVoltaX[i]:
                j += 1
            k += 1
            if k == 512:
                listaFrequenciaX.append(j)
                k = 0
                j = 0
# calcula frequencias Y
        for i in range(len(freqIdaY)):
            if freqIdaY[i] == freqVoltaY[i]:
                j += 1
            k += 1
            if k == 512:
                listaFrequenciaY.append(j)
                k = 0
                j = 0
# calcula frequencias Z
        for i in range(len(freqIdaZ)):
            if freqIdaZ[i] == freqVoltaZ[i]:
                j += 1
            k += 1
            if k == 512:
                listaFrequenciaZ.append(j)
                k = 0
                j = 0
        contagemFrequenciaX = ct(listaFrequenciaX)
        media = 0.0
        variancia = 0.0
        desvio = 0.0
        qtd = 0.0
#print resultados
        print(ninho+'-'+tratamento)
        print('media X = ' +str(calcMedia(listaFrequenciaX)), 'desvio = '+str(calcDesvio(listaFrequenciaX)), 'Min: '+ str(min(listaFrequenciaX)), 'Max: '+str(max(listaFrequenciaX)))
        print('media Y = ' +str(calcMedia(listaFrequenciaY)), 'desvio = '+str(calcDesvio(listaFrequenciaY)), 'Min: '+ str(min(listaFrequenciaY)), 'Max: '+str(max(listaFrequenciaY)))
        print('media Z = ' +str(calcMedia(listaFrequenciaZ)), 'desvio = '+str(calcDesvio(listaFrequenciaZ)), 'Min: '+ str(min(listaFrequenciaZ)), 'Max: '+str(max(listaFrequenciaZ)))
        print(sorted(contagemFrequenciaX))
#exportando para csv
        writer.writerow(listaFrequenciaX)
        writer.writerow(listaFrequenciaY)
        writer.writerow(listaFrequenciaZ)
#plotando gráficos
#        if ninho == "N04YCC2017":
#            plt.plot(listaFrequenciaX)
#            plt.plot(listaFrequenciaY)
#            plt.plot(listaFrequenciaZ)
#            plt.show()
connection.close()
result.close
