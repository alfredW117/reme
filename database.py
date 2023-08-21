import psycopg2
def obtener_conexion():
    conn = psycopg2.connect(host='localhost', port=5432, database='server', user='postgres', password='ixmiquilpan')
    if conn is None:
        print('Error connecting')
    else:
        print('Connection established')
    return conn

"""if _name_ == '_main_':
obtener_conexion()"""
