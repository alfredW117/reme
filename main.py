from flask import Flask, render_template, request, redirect
from src.model.modelo_dispositivo import insertar_dispositivo, consultar_dispositivo, modificar_dispositivo,obtener_conexion

app = Flask(_name_)


@app.route('/')
def index():
    example-app-1234567890ab.herokuapp.com


@app.route('/datos_dipo', methods=['POST'])
def datos_dispo():
    id_server=request.form["id_server"]
    servidor=request.form["servidor"]
    url=request.form["url"]
    estatus=request.form["estatus"]
    metodo=request.form["metodo"]
    tiempo=request.form["tiempo"]
    fecha=request.form["fecha"]
    valor =insertar_dispositivo( id_server, servidor, url, estatus, metodo, tiempo,fecha )
    return "Registro correcto"


@app.route('/form_editar_dispo/<id>')
def form_editar_dispo(id):
    return render_template("for_editar_dispo.html") #importante anexar " lista=lista_dispositivo "

@app.route('/datos_editar_dispo', methods=['POST'])
def modificar_dispositivo():
    servidor = request.form["servidor"]
    url = request.form["url"]
    estatus = request.form["estatus"]
    metodo = request.form["metodo"]
    tiempo = request.form["tiempo"]
    fecha = request.form["fecha"]
    id_server = request.form["id_server"]
    valor = insertar_dispositivo(id_server, servidor, url, estatus, metodo, tiempo, fecha )
    return redirect('/datos_editar_dispo')

@app.route("/form_eliminar_dispo/<id>")
def form_eliminar_dispositivo(id):
    conn = obtener_conexion()
    cur_conn = conn.cursor()
    query = "DELETE FROM servers WHERE id_server = "+ id +""
    cur_conn.execute(query, (id,))
    conn.commit()
    conn.close()
    cur_conn.close()
    return redirect('/')

#----------------------------------------------------------------

@app.route("/datos_dispo/" , methods=["POST"])
def guardar():
    estatus = request.form['estatus']
    conn = obtener_conexion()
    cursor = conn.cursor()
    insert_query = "INSERT INTO estatus (estatus) VALUES (%s)"
    cursor.execute(insert_query, (estatus,))
    conn.commit()
    cursor.close()

    return "Datos almacenados en la base de datos con éxito."


@app.route("/datos_dispo/" , methods=["POST"])
def save():
    metodo = request.form['metodo']
    conn = obtener_conexion()
    cursor = conn.cursor()
    insert_query = "INSERT INTO metodo (estatus) VALUES (%s)"
    cursor.execute(insert_query, (metodo,))
    conn.commit()
    cursor.close()

    return "Datos almacenados en la base de datos con éxito."

#----------------------------------------------------------------
