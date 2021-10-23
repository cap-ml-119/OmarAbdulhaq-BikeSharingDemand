from flask import jsonify, request
from app import app
from prediction import PickledModel
from werkzeug.datastructures import FileStorage
import numpy as np
import pandas as pd
import pickle
from io import StringIO
from sklearn.pipeline import Pipeline


@app.route("api/v1/SinglePrediction", methods = ["POST"])
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
        predict = float(PickledModel.SimplePred(data))

    except:
        response = jsonify({
            'status': '400',
            'msg': 'Samples don\'t match, make sure of the entered Sample name.'
        })
    
    else:
        response = jsonify({
            'status': '200',
            'prediction': predict
        })

    return response


with open("model.csv", "rb") as csv:
    file_dict = {"model.csv": csv}
    res = request.post("http://httpbin.org/post", files=file_dict)


@app.route("", methods = [""])
def BatchPrediction():

    try:
        read_csv = request.files.get("model.csv", FileStorage())

        dataframe = pd.read_csv(
            StringIO(read_csv.stream.read().decode("utf-8")))


        modelpred = pipeline.predict(dataframe)


    except:

        response = jsonify({
            'status': '400',
            'msg': 'sent Model doesn\'t match, make sure to enter the Model name correctly.'
        })

    
    else:
        response = jsonify({
            'status': '200',
            'prediction': modelpred
        })
