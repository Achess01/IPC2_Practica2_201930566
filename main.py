from flask import Flask, request
from flask import json
import flask
from flask.helpers import make_response
from flask.json import jsonify
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

@app.route('/see_all', methods=['GET'])
def see_all():
    data = get_data()
    print("MÉTODO GET","Datos devueltos")
    print(data)
    print("*"*10)
    return jsonify(get_data())

@app.route('/edit_podcast', methods=['PUT'])
def edit_podcast():
    pass

@app.route('/delete_podcast', methods=['DELETE'])
def delete_podcast():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=4000)