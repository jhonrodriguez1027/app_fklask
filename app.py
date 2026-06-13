from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

modelo = load("modelo.kmeans.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    ingresos = float(request.form["ingresos"])
    gastos = float(request.form["gastos"])

    datos = np.array([[ingresos, gastos]])

    cluster = modelo.predict(datos)[0]

    return render_template(
        "index.html",
        prediccion=f"El cliente pertenece al grupo {cluster}"
    )

if __name__ == "__main__":
    app.run(debug=True)