from src.config.database import obtener_conexion

def insertar_dispositivo( id_server, servidor, url, estatus, metodo, tiempo,fecha ):
    conn= obtener_conexion()
    query = "INSERT INTO public.servers (id_server, servidor, url, estatus, metodo, tiempo, fecha ) VALUES ('"+id_server+"','"+servidor+"','"+url+"','"+estatus+"','"+metodo+"','"+tiempo+"','"+fecha+"');"
    cur_conn = conn.cursor()
    valor= cur_conn.execute(query)
    conn.commit()
    cur_conn.close()
    conn.close()
    return valor

def modificar_dispositivo(id_server, servidor, url, estatus, metodo, tiempo,fecha):
    conn= obtener_conexion()
    query = "UPDATE public.servers SET (servidor '"+servidor+"', url '"+url+"', estatus '"+estatus+"', metodo '"+metodo+"', tiempo '"+tiempo+"', fecha '"+fecha+"' ) WHERE id = "+id_server+"' ;"
    cur_conn= conn.cursor()
    valor=cur_conn.execute(query)
    ldispositivos= cur_conn.fetchall()
    conn.close()
    return ldispositivos

def consultar_dispositivo():
    conn= obtener_conexion()
    query = "SELECT * FROM servers ;"
    cur_conn= conn.cursor()
    valor=cur_conn.execute(query)
    layuda= cur_conn.fetchall()
    conn.close()
    cur_conn.close()
    return layuda
