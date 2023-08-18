
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import obtener_conexion

def insertar_dtos(servidor, url, estatus, metodos, fecha, tiempo, id_monitoreo):
    conn=obtener_conexion()
    query= "INSERT INTO servicios VALUES('"+servidor+"','"+url+"','"+estatus+"','"+metodos+"','"+fecha+"', '"+tiempo+"',"+id_monitoreo+");"
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(query)
    return "datos insertados correctamente"

def consultar_servicio():
    conn=obtener_conexion()
    query= "SELECT * FROM servicios"
    cursor= conn.cursor()
    valor =cursor.execute(query)
    lservicios =cursor.fetchall()
    cursor.close()
    conn.close()
    print(lservicios)
    return lservicios

def consultar_servicio1(id):
    conn=obtener_conexion()
    query= "SELECT * FROM servicios where Servidor='"+id+"';"
    cursor= conn.cursor()
    valor =cursor.execute(query)
    lservicios =cursor.fetchone()
    cursor.close()
    conn.close()
    print(lservicios)
    return lservicios

def modificar_serv(servidor, url, estatus, metodos, fecha, tiempo, id_monitoreo):
    conn=obtener_conexion()
    query="UPDATE servicios SET Url='"+url+"', Estatus='"+estatus+"', Metodos='"+metodos+"', Fecha='"+fecha+"', Tiempo='"+tiempo+"', id_monitoreo="+id_monitoreo+" WHERE Servidor='"+servidor+"';"
    cursor=conn.cursor()
    valor=cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    return valor

  

def borrar_serv(id):
    conn=obtener_conexion()
    query="DELETE FROM servicios where servidor='"+id+"';"
    cursor=conn.cursor()
    valor=cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    return valor