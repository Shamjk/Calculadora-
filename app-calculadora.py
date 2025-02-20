from flask import Flask  ## Flask es un microframework para el uso de Python en la web
from flask_cors import CORS  ## Necesario para configurar acceso de programas de terceros
import math as mt  ## Librería que implementa funciones matemáticas
from flask import jsonify  ## Para retornar las respuestas en formato JSON

app = Flask(__name__)
CORS(app)

## Suma
@app.route("/suma/<int:numero1>/<int:numero2>")
def suma(numero1=0, numero2=0):
    resultado = numero1 + numero2
    data = {
        "Resultado": resultado,
        "Operacion": "suma",
    }
    return jsonify(data)


## Resta
@app.route("/resta/<int:numero1>/<int:numero2>")
def resta(numero1=0, numero2=0):
    resultado = numero1 - numero2
    data = {
        "Resultado": resultado,
        "Operacion": "resta",
    }
    return jsonify(data)

## Multiplicación
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
def multiplicacion(numero1=0, numero2=0):
    resultado = numero1 * numero2
    data = {
        "Resultado": resultado,
        "Operacion": "multiplicación",
    }
    return jsonify(data)

## División
@app.route("/division/<int:numero1>/<int:numero2>")
def division(numero1=0, numero2=0):
    resultado = numero1 / numero2 if numero2 != 0 else "Error: División por cero"
    data = {
        "Resultado": resultado,
        "Operacion": "División",
    }
    return jsonify(data)

## Potenciación
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
def potenciacion(numero1=0, numero2=0):
    resultado = numero1 ** numero2
    data = {
        "Resultado": resultado,
        "Operacion": "potenciación",
    }
    return jsonify(data)

## Seno
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    resultado = mt.sin(numero1)
    data = {
        "Resultado": resultado,
        "Operacion": "seno",
    }
    return jsonify(data)

## Coseno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    resultado = mt.cos(numero1)
    data = {
        "Resultado": resultado,
        "Operacion": "coseno",
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
