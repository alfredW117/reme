import psycopg2
def obtener_conexion():
    conn = psycopg2.connect(host='ec2-52-206-36-147.compute-1.amazonaws.com', port=5432, database='server', user='fygmqqygxiketd', password='a5b93a5445a3906910014ca6d7824e8153087e98311d0ebac475b74a0d8d62b6')
    if conn is None:
        print('Error connecting')
    else:
        print('Connection established')
    return conn

"""if _name_ == '_main_':
obtener_conexion()"""
