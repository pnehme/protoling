import psycopg2 as pg
def exec_con():
    return pg.connect("dbname=protoling user=postgres password=lucas2004")
def exec_sql(sql):
    return exec_con.prepare(sql)
