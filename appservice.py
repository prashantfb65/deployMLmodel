from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
import joblib
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def return_prediction(model, scaler, sample_json):
    sepal_length = sample_json['sepal_length']
    sepal_width = sample_json['sepal_width']
    petal_length = sample_json['petal_length']
    petal_width = sample_json['petal_width']
    classes = np.array(['setosa', 'versicolor', 'virginica'])
    flower = [[sepal_length, sepal_width, petal_length, petal_width]]
    flower = scaler.transform(flower)
    class_index = model.predict_classes(flower)
    return classes[class_index][0]

app = Flask(__name__)

classification_model = load_model('model/iris_classification_model.h5')
classification_scaler = joblib.load('model/iris_classification_scaler.pkl')

@app.route("/")
def index():
    return '<h1> Flask app is running </h1>'

@app.route("/api/flower", methods=['POST'])
def flower_prediction():
    content = request.json
    results = return_prediction(classification_model, classification_scaler, content)
    return jsonify({'prediction' :results})

if __name__=='__main__':
    app.run(port=9090)
