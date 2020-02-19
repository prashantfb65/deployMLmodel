from flask import Flask, render_template, session, url_for, redirect
import numpy as np
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
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
app.config['SECRET_KEY'] = 'secret_key'

classification_model = load_model('model/iris_classification_model.h5')
classification_scaler = joblib.load('model/iris_classification_scaler.pkl')

class FlowerForm(FlaskForm):
    sep_len = TextField("Sepal Length")
    sep_wid = TextField("Speal Width")
    pet_len = TextField("Petal Length")
    pet_wid = TextField("Petal Width")
    submit = SubmitField("Analyze")

@app.route("/", methods=['GET', 'POST'])
def index():
    form = FlowerForm()
    if form.validate_on_submit():
        session['sep_len'] = form.sep_len.data
        session['sep_wid'] = form.sep_wid.data
        session['pet_len'] = form.pet_len.data
        session['pet_wid'] = form.pet_wid.data
        return redirect(url_for("prediction"))
    return render_template('home.html', form=form)

@app.route("/prediction")
def prediction():
    content = {}
    content['sepal_length'] = float(session['sep_len'])
    content['sepal_width'] = float(session['sep_wid'])
    content['petal_length'] = float(session['pet_len'])
    content['petal_width'] = float(session['pet_wid'])
    results = return_prediction(classification_model, classification_scaler, content)
    return render_template('prediction.html', results=results)

if __name__=='__main__':
    app.run(port=9090)
