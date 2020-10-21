from pg_db import acc_db as acc
import pandas as pd
import matplotlib.pyplot as plt
import csv
connection = acc.exec_con()
result = open("c:/BASE1/resultado_frequencias.csv",'w')
writer = csv.writer(result, delimiter=",", lineterminator="\n", dialect = 'excel')
for i in range(1,5):
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
            if i > valAnt:
                freqIdaX.append(1)
            elif i == valAnt:
                freqIdaX.append(0)
            else:
                freqIdaX.append(-1)
            valAnt = i
#        print('ida')
        valAnt = 0
        for i in df['a_y']:
            if i > valAnt:
                freqIdaY.append(1)
            elif i == valAnt:
                freqIdaY.append(0)
            else:
                freqIdaY.append(-1)
            valAnt = i
        valAnt = 0
        for i in df['a_z']:
            if i > valAnt:
                freqIdaZ.append(1)
            elif i == valAnt:
                freqIdaZ.append(0)
            else:
                freqIdaZ.append(-1)
            valAnt = i
        df1 = df.sort_values('r_time',ascending=False)
        valAnt = 0
        for i in df1['a_x']:
            if i > valAnt:
                freqVoltaX.append(1)
            elif i == valAnt:
                freqVoltaX.append(0)
            else:
                freqVoltaX.append(-1)
            valAnt = i
        valAnt = 0
        for i in df1['a_y']:
            if i > valAnt:
                freqVoltaY.append(1)
            elif i == valAnt:
                freqVoltaY.append(0)
            else:
                freqVoltaY.append(-1)
            valAnt = i
        valAnt = 0
        for i in df1['a_z']:
            if i > valAnt:
                freqVoltaZ.append(1)
            elif i == valAnt:
                freqVoltaZ.append(0)
            else:
                freqVoltaZ.append(-1)
            valAnt = i
        i = 0
        j = 0
        k = 0
#        print('volta')
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

        print(ninho+'-'+tratamento)
#        print(listaFrequencia)
        writer.writerow(listaFrequenciaX)
        writer.writerow(listaFrequenciaY)
        writer.writerow(listaFrequenciaZ)
        if ninho == "N04YCC2017":
            plt.plot(listaFrequenciaX)
            plt.plot(listaFrequenciaY)
            plt.plot(listaFrequenciaZ)
            plt.show()
connection.close()
result.close
