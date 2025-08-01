from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Simulación de predicción
    data = request.get_json()
    result = {"prediction": "positivo" if data else "negativo"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
