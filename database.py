import psycopg2

#hacer conexion bd
def obtener_conexion():
    conn = psycopg2.connect(host='ec2-44-212-250-48.compute-1.amazonaws.com', port=5432, database='daprs7gajn8iue', user='uxkmtjlhyxabiw', password='57f31dea73be201545726868c0a3ddffe9d07bc66c2500113f40b24224f4a38c')
    if conn is None:
        print('Error al conectar a la base de datos')
    else:
        print("Conexion a la base de datos exitosa")

    return conn
if __name__ == '__main__':
    obtener_conexion()