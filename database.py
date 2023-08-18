import psycopg2

#hacer conexion bd
def obtener_conexion():
    conn = psycopg2.connect(host='localhost', port=5432, database='monitoreo_servidores', user='postgres', password='cisco123')
    if conn is None:
        print('Error al conectar a la base de datos')
    else:
        print("Conexion a la base de datos exitosa")

    return conn
if __name__ == '__main__':
    obtener_conexion()