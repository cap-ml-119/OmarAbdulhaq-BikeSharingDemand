from flask import jsonify, request, Blueprint
import numpy as np
import pandas as pd
import pickle
from io import StringIO
from werkzeug.wrappers import Response

PreApi: Blueprint = Blueprint(
    'PreApi', __name__, url_prefix='/api/v1')

with open("./app/model.sav", "rb") as model:
    result = pickle.load(model)


@PreApi.route("/SinglePrediction", methods=['POST'])
def SinglePrediction():
    try:
        workingdays = np.float64(request.form['workingsday'])
        weather = np.float64(request.form['weather'])
        temp = np.float64(request.form['temp'])
        humidity = np.float64(request.form['humidity'])
        windspeed = np.float64(request.form['windspeed'])
        days = np.float64(request.form['days'])
        seconds = np.float64(request.form['seconds'])

        data = [workingdays, weather, temp, humidity, windspeed, days, seconds]

        predict = {"Prediction": np.float64(result.predict([data]))}
        response = jsonify({
            'status': '200',
            'prediction': predict
        })

    except Exception:
        response = jsonify({
            'status': '400',
            'msg': 'Samples don\'t match, make sure of the entered Sample name.'
        })
    return response


@PreApi.route("/PatchPrediction", methods=["POST"])
def PatchPrediction():
    try:
        if 'File' not in request.files:
            raise Exception("Please make sure you're attaching a file")
        df = pd.read_csv(
            StringIO(request.files['File'].read().decode('utf-8')))
        modelPred = result.predict(df)
        PatchDF = []
        for line in modelPred:
            PatchDF.append(str(line)+'\n')
        response = Response(PatchDF, mimetype='text/csv')

    except Exception:

        response = jsonify({
            'status': '400',
            'msg': 'sent Model doesn\'t match, make sure to enter the Model name correctly.'
        })

    return response
