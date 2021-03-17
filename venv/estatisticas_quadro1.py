from pg_db import acc_db as acc
import pandas as pd
#estabelece a conexão com o banco de dados
connection = acc.exec_con()
#Saída dos resiltados para arquivo csv
file = open("c:/BASE1/resultado_estatisticas.csv","w")
file.write('ninho , tratamento , MédiaX , MédiaY , MédiaZ , Std(X) , Std(Y) , Std(Z) , Máx(X) , Min(X) , Máx(Y) , Min(Y) ,  Máx(Z) , Min(Z) \n')

for i in range(1,16):
    if i < 10:
        ninho = 'N0'+str(i)+'YCC2017'
    else:
        ninho = 'N'+str(i)+'YCC2017'
    for j in range(1,5):
        tratamento = 'T0'+str(j)
#executa a consulta ao banco e cria o dataframe pandas para cada ninho e tratamento
        df = pd.read_sql_query("select nest_id, treatment, a_x, a_y, a_z, r_time from data_vibration_1 where nest_id = '"+ninho+"' and treatment = '"+tratamento+"' order by r_time", connection)
#cálculo estatístico
        mediax = str(format(df['a_x'].mean(), '.2f'))
        mediay = str(format(df['a_y'].mean(), '.2f'))
        mediaz = str(format(df['a_z'].mean(), '.2f'))
        sigmax = str(format(df['a_x'].std(), '.2f'))
        sigmay = str(format(df['a_y'].std(), '.2f'))
        sigmaz = str(format(df['a_z'].std(), '.2f'))
        minx = str(df['a_x'].min())
        maxx = str(df['a_x'].max())
        miny = str(df['a_y'].min())
        maxy = str(df['a_y'].max())
        minz = str(df['a_z'].min())
        maxz = str(df['a_z'].max())
# exportando para arquivo csv
        file.write(ninho + ',' + tratamento + ',' + mediax + ',' + mediay + ',' + mediaz + ',' + sigmax + ',' + sigmay + ',' + sigmaz + ',' + maxx + ',' + minx + ',' + maxy + ',' + miny + ',' + maxz + ',' + minz + '\n')
        print(ninho + '-' + tratamento)
file.close()
connection.close()

