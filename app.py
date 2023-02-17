from flask import Flask
from flask import (
    render_template
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/aviso-privacidad", methods=["GET"])
def aviso_privacidad():
    return render_template("aviso-privacidad.html")


@app.route("/boletos", methods=["GET"])
def boletos():
    numeros = []
    for numero in range(10000):
        numeros.append(str(numero).zfill(4))

    return render_template("boletos.html", numeros=numeros)