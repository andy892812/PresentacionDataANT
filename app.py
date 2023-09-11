from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configuramos la base de datos
cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['PruebaFinal']
base = db['citaciones']

@app.route('/')
def index():
    # Consulta la base de datos y devuelve los datos
    datos = list(base.find())
    return render_template('index.html', datos=datos)

@app.route('/api/datos')
def obtener_datos():
    # Consulta la base de datos y devuelve los datos en formato JSON
    datos = list(base.find({}, {'infraccion': 0,
    'entidad': 1,
    'citacion': 2,
    'placa': 3,
    'fechaemision': 4,
    'fechanotificacion': 5,
    'sancion': 6,
    'puntos': 7,
    'multa': 8,
    'remision': 9,
    'totalpagar': 10,
    'articulo': 11}))
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)