from flask import Flask, request, jsonify
from flask_cors import CORS
import h2o
import pandas as pd

h2o.init()
model = h2o.load_model("./modelos_guardados/GBM_2_AutoML_1_20250731_190306")

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        frame = h2o.H2OFrame(df)
        prediction = model.predict(frame)
        pred_df = prediction.as_data_frame()
        predicted_class = int(pred_df.iloc[0, 0])  # Primera columna = clase

        return jsonify({
            "class": predicted_class,
            "probabilities": pred_df.to_dict()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

