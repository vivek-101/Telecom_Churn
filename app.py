import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from preprocessing import keep,feature_ext

app = Flask(__name__)
model = pickle.load(open('churn_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    value = [x for x in request.form.values()]
    sample = feature_ext(pd.DataFrame(np.array(value).reshape(-1,20)))
    prediction = model.predict_proba(sample[keep])[0][1]

    if prediction <= 0.3:
        output = 'Leave'
    else:
        output = 'Stay'
    return render_template('index.html', prediction_text='The customer is likely to {}'.format(output))

@app.route('/predict_api',methods=['Post'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict[np.array(list(data.values()))]

    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run()
