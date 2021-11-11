from flask import Flask, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from model_cantidad import Cantidad
from model_carrito import Carrito
import db_crud_cantidad
import db_crud_carrito
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carrito.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)


@app.route("/carrito", methods=['GET'])
def principal():
    data = db_crud_carrito.get_all(Carrito)
    diccionario_carrito = []
    for d in data:
        p = {
            "id": d.id,
            "estado": d.status_carrito,
            "fecha": d.date_carrito,
            "customer_id": d.customer_id_fk
        }
        diccionario_carrito.append(p)
    return json.dumps(diccionario_carrito), 200

@app.route("/cantidad", methods=['GET'])
def principal():
    data = db_crud_cantidad.get_all(Cantidad)
    diccionario_cantidad = []
    for d in data:
        p = {
            "cantidad_total": d.cliente_nombre,
            "producto_id": d.producto_id_fk,
            "carrito_id": d.carrito_id_fk
        }
        diccionario_cantidad.append(p)
    return json.dumps(diccionario_cantidad), 200




@app.route("/carrito/agregar", methods=['POST'])
def agregar():
    data = json.loads(request.data)
    datos = {
        "estado": data["estado"],
        "fecha": data["fecha"],
        "customer_id": data["customer_id"]
    }
    db_crud_carrito.add_instance(Carrito, datos)
    return json.dumps("Elemento Agregado "+str(datos)), 200


@app.route("/cantidad/agregar", methods=['POST'])
def agregar():
    data = json.loads(request.data)
    datos = {
        "cantidad_total": data["cantidad_total"],
        "product_id": data["product_id"],
        "carrito_id": data["carrito_id"]
    }
    db_crud_cantidad.add_instance(Cantidad, datos)
    return json.dumps("Elemento Agregado "+str(datos)), 200

#i need a method tho delete a specific carrito
@app.route("/carrito/eliminar/<int:id>", methods=['DELETE'])
def eliminar(id):
    db_crud_carrito.delete_instance(Carrito, id)
    return json.dumps("Elemento Eliminado"), 200

#i need a method tho delete a specific cantidad
@app.route("/cantidad/eliminar/<int:id_producto>/<int:id_carrito>", methods=['DELETE'])
def eliminar(id_producto,id_carrito):
    db_crud_cantidad.delete_instance(Cantidad, id_producto,id_carrito)
    return json.dumps("Elemento Eliminado"), 200


@app.route("/carrito/actualizar/<int:id>", methods=['PATCH'])
def actualizar(id):
    data = json.loads(request.data)
    db_crud_carrito.edit_instance(Carrito, id, data)
    return json.dumps("Elemento Editado "+str(id)), 200

@app.route("/cantidad/actualizar/<int:id_producto>/<int:id_carrito>", methods=['PATCH'])
def actualizar(id_producto,id_carrito):
    data = json.loads(request.data)
    db_crud_cantidad.edit_instance(Cantidad, id_producto,id_carrito, data)
    return json.dumps("Elemento Editado "+str(id_producto,id_carrito)), 200


#i need a method to search specific carrito
@app.route("/carrito/buscar/<int:id>", methods=['GET'])
def buscar(id):
    data = db_crud_carrito.get_by_id(Carrito, id)
    p = {
        "id": data.id,
        "estado": data.status_carrito,
        "fecha": data.date_carrito,
        "customer_id": data.customer_id_fk
        }
        
    return json.dumps(p), 200


#i need a method to search specific cantidad
@app.route("/cantidad/buscar/<int:id_producto>/<int:id_carrito>", methods=['GET'])
def buscar(id_producto,id_carrito):
    data = db_crud_cantidad.get_by_id(Cantidad, id_producto,id_carrito)
    p = {
        "cantidad_total": data.cliente_nombre,
        "producto_id": data.producto_id_fk,
        "carrito_id": data.carrito_id_fk
        }
        
    return json.dumps(p), 200


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)