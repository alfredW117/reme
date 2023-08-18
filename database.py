import psycopg2

#hacer conexion bd
def obtener_conexion():
    conn = psycopg2.connect(host='ec2-52-206-36-147.compute-1.amazonaws.com', port=5432, database='d5j7em44t5al2j', user='fygmqqygxiketd', password='a5b93a5445a3906910014ca6d7824e8153087e98311d0ebac475b74a0d8d62b6')
    if conn is None:
        print('Error al conectar a la base de datos')
    else:
        print("Conexion a la base de datos exitosa")

    return conn
if __name__ == '__main__':
    obtener_conexion()