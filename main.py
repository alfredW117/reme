from flask import Flask, render_template, request, redirect
from model_u import insertar_dtos,consultar_servicio, modificar_serv, consultar_servicio1,borrar_serv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




app = Flask(__name__)


@app.route('/')
def index():
    return render_template("inicio.html")





@app.route("/registrar")
def datos_regi():
    lista=consultar_servicio()
    return render_template('form_registrar.html',lserv=lista)

@app.route("/datos_regis", methods=["POST"])
def datos_regis():
    servidor=request.form["servi"]
    url=request.form["url"]
    estatus=request.form["estatus"]
    metodo=request.form["metodo"]
    fecha=request.form["fecha_R"]
    tiempo=request.form["tiempo"]
    ID_monitoreo= request.form["id_m"]

    valor =insertar_dtos(servidor, url, estatus, metodo,fecha,tiempo, ID_monitoreo)
    print(valor)
    return redirect("/registrar")


@app.route("/editar_serv/<id>")
def editar_serv(id):
    lista_serv=consultar_servicio1(id)
    return render_template('editar_servicio.html',lserv = lista_serv)

@app.route("/editar_datos_serv", methods=["POST"])
def editar_datos_serv():
    servidor=request.form["servi"]
    url=request.form["url"]
    estatus=request.form["estatus"]
    metodo=request.form["metodo"]
    fecha=request.form["fecha_R"]
    tiempo=request.form["tiempo"]
    ID_monitoreo= request.form["id_m"]

    update_serv =modificar_serv(servidor, url, estatus, metodo,fecha,tiempo, ID_monitoreo)
    return redirect("/registrar")
   
@app.route("/eliminar_serv/<id>")
def eliminar_serv(id):
    borrar_serv(id)
    return redirect('/registrar')

if __name__ == '__main__':
    app.run(debug=True)