import pickle
from flask import Flask, request, jsonify, render_template, app, url_for
import numpy as np
import pandas as pd
import sklearn

app = Flask(__name__)

#load the model

regmodel = pickle.load(open('regression_model.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))

    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    result = regmodel.predict(new_data)
    print(result[0])
    return jsonify({'prediction': result[0]})

if __name__ == "__main__":
    app.run(debug=True)
    