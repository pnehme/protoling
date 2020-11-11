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

def comparaAmplitude(x, minimo, maximo):
    valor = ''
    passo = 0
    codigo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    passo = maximo - minimo
    passo = passo / 20
    for i in range(21):
        if minimo + passo * (i - 1) <= x < minimo + passo * i:
           valor = codigo[i - 1]
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
        mediax = df['a_x'].mean()
        mediay = df['a_y'].mean()
        mediaz = df['a_z'].mean()
        sigmax = df['a_x'].std()
        sigmay = df['a_y'].std()
        sigmaz = df['a_z'].std()
        minx = df['a_x'].min()
        maxx = df['a_x'].max()
        miny = df['a_y'].min()
        maxy = df['a_y'].max()
        minz = df['a_z'].min()
        maxz = df['a_z'].max()
        ampX = ''
        ampY = ''
        ampZ = ''
        palavra = ''
        limite = 1.5
#        print(mediax, sigmax, minx, maxx)
#        print(mediay, sigmay, miny, maxy)
#        print(mediaz, sigmaz, minz, maxz)
        file.write(ninho+'-'+tratamento+'\n')
        for rows in df.itertuples():
            if (rows.a_x > mediax + limite * sigmax) or (rows.a_x < mediax - limite * sigmax):
                ampX = comparaAmplitude(rows.a_x, minx, maxx)
            if (rows.a_y > mediay + limite * sigmay) or (rows.a_y < mediay - limite * sigmay):
                ampY = comparaAmplitude(rows.a_y, miny, maxy)
            if (rows.a_z > mediaz + limite * sigmaz) or (rows.a_z < mediaz - limite * sigmaz):
                ampZ = comparaAmplitude(rows.a_z, minz, maxz)
            if (ampX + ampY + ampZ) != '':
                palavra = palavra + ampX + ampY + ampZ + ' '
            i += 1
            if i == 512:
                file.write(palavra + ' * ')
                i = 0
                palavra = ''
        file.write('\n')
        print(ninho+'-'+tratamento)

#exportando para csv
#        writer.writerow(picoXYZ)
#        file.write(picoXYZ)
file.close()
#result.close
connection.close()

