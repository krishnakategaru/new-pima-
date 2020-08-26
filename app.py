# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:55:37 2020

@author: srisaikrishna.k
"""
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_1.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    prediction_texts='em ra ravatle'
    if request.method == 'POST':
        pregnant=int(request.form['pregnant'])
        bp=float(request.form['bp'])
        insulin=float(request.form['insulin'])
        tricep=float(request.form['tricep'])
        glucose=float(request.form['glucose'])
        bmi=float(request.form['bmi'])
        age=float(request.form['age'])
        dpf=float(request.form['dpf'])
        
        prediction=model.predict([[pregnant,glucose,bp,tricep,insulin,bmi,dpf,age]])
        output=prediction
        if output==1:
            return render_template('index_1.html',prediction_texts="Hey, you are diabetic, may god help you")
        else:
            return render_template('index_1.html',prediction_texts="No need to worry, your not diabetic")
    else:
        return render_template('index_1.html')

if __name__=="__main__":
    app.run(debug=True)