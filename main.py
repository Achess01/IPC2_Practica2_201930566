from flask import Flask, request
import flask
from flask.helpers import make_response
from flask.json import jsonify
from flask.wrappers import Response
from src.manage_data import *


app = Flask(__name__)

@app.route('/')
def ping():
    return jsonify({"Message": "Pequeña API sobre algunos de los podcasts que escucho."})

@app.route('/add_podcast', methods=['POST'])
def add_podcast():     
    try:
        data = request.data
        print("MÉTODO POST","Datos recibidos")
        print(data)
        print("*"*10)
        add_data(data)
        return jsonify({"Message": "Datos agregados"})
    except ValueError:
        return jsonify({"Message": "Datos no agregados"})

@app.route('/podcasts', methods=['GET'])
def see_all():
    data = get_data()
    print("MÉTODO GET","Datos devueltos")
    print(data)
    print("*"*10)
    return jsonify(get_data())

@app.route('/podcasts/<int:id>', methods=['PUT'])
def edit_podcast(id):
    data = request.data
    print("MÉTODO PUT")
    response = edit_data(id, data)
    if response != None:
        print("Datos modificados")
        print(response)
        return jsonify(response)
    else:
        print("Los datos no fueron modificados")
        return jsonify({"Message": "Datos no agregados"})


@app.route('/delete_podcast/<int:id>', methods=['DELETE'])
def delete_podcast(id):
    print("MÉTODO DELETE")
    response = delete_data(id)
    if response != None:
        print("Datos eliminados")
        print(response)
        return jsonify({"Message": "Datos eliminados", "Datos": response})
    else:
        return jsonify({"Message": "Datos no eliminados"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)