from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ingresos = float(request.form['ingresos'])
    gastos = float(request.form['gastos'])
    # Aquí iría la lógica para hacer la predicción con el modelo cargado
    return render_template('index.html')  # O redirigir a una página de resultados

if __name__ == '__main__':
    app.run(debug=True)