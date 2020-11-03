from pg_db import acc_db as acc
import pandas as pd
import matplotlib.pyplot as plt
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

def comparaAmplitude(x, mediax, sdx):
    valor = ''
    codigo_sup = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
    codigo_inf = ['A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0', 'I0', 'J0', 'K0', 'L0', 'M0', 'N0', 'O0', 'P0', 'Q0', 'R0', 'S0', 'T0']
    if x > mediax + 2 * sdx:
        for i in range(21):
            if (mediax + 2 * sdx) * (1 + 5 * (i-1) * 0.01) <= x < (mediax + 2 * sdx) * (1 + 5 * i * 0.01):
                valor = codigo_sup[i-1]
    elif x < mediax - 2 * sdx:
        for i in range(21):
            if (mediax - 2 * sdx) * (1 + 5 * (i) * 0.01) <= x < (mediax - 2 * sdx) * (1 + 5 * (i - 1) * 0.01):
                valor = codigo_inf[i-1]
    else:
        valor = '*'
    return valor

connection = acc.exec_con()
#result = open("c:/BASE1/resultado_amplitudes.csv",'w')
#writer = csv.writer(result, delimiter=",", lineterminator="\n", dialect = 'excel')
file = open("c:/BASE1/resultado_amplitudes.txt","w")
for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)+'YCC2017'
    else:
        ninho = 'N'+str(i)+'YCC2017'
    for j in range(1,5):
        tratamento = 'T0'+str(j)
        df = pd.read_sql_query("select nest_id, treatment, a_x, a_y, a_z, r_time from data_frequency where nest_id = '"+ninho+"' and treatment = '"+tratamento+"' order by nest_id, treatment, r_time", connection)

#cálculo dos picos de amplitude > 2sigma para X
        xbarra = calcMedia(df['a_x'])
        ybarra = calcMedia(df['a_y'])
        zbarra = calcMedia(df['a_z'])
        xsigma = calcDesvio(df['a_x'])
        ysigma = calcDesvio(df['a_y'])
        zsigma = calcDesvio(df['a_z'])
        picoXYZ = [[],[],[]]
        ampX = ''
        ampY = ''
        ampZ = ''
        palavra = ''
        file.write(ninho+'-'+tratamento)
        for index, rows in df.iterrows():
            ampX = comparaAmplitude(rows['a_x'], xbarra, xsigma)
            ampY = comparaAmplitude(rows['a_y'], ybarra, ysigma)
            ampZ = comparaAmplitude(rows['a_z'], zbarra, zsigma)
            palavra = palavra + ampX + ampY + ampZ
            i += 1
            if i == 512:
                file.write(palavra + '/n')
                i = 0
                palavra = ''
        print(ninho+'-'+tratamento)

#exportando para csv
#        writer.writerow(picoXYZ)
#        file.write(picoXYZ)
file.close()
#result.close
connection.close()

