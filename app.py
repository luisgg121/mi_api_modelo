{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "343cfd38-ea54-459c-96f1-6774d04f5ebc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Código Flask\n",
    "\n",
    "from flask import Flask, request, jsonify\n",
    "import h2o\n",
    "\n",
    "h2o.init()\n",
    "model = h2o.load_model(\"modelo/GBM_2_AutoML_1_20250731_190306\")\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    frame = h2o.H2OFrame(data)\n",
    "    prediction = model.predict(frame)\n",
    "    return jsonify(prediction.as_data_frame().to_dict())\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='0.0.0.0', port=8080)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
