import datetime as dt
from flask import Flask, request
from ie_bike_model.util import read_data
from ie_bike_model.model import predict

app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return "Hello, " + name + "!"


@app.route("/predict")
def get_predict():

    # Tried to input the average when inputs are not specified, but couldnt make it

    #df = read_data()
    #weather_avg = df['weathersit'].mean()
    #temp_avg = df['temperature_C'].mean()
    #feeling_avg = df['feeling_temperature_C'].mean()
    #humidity_avg = df["humidity"].mean()
    #windspeed_avg = df["windspeed"].mean()

    #parameters["date"] = dt.datetime.fromisoformat(parameters["date"])
    #parameters["weathersit"] = int(parameters.get("weathersit", weather_avg))
    #parameters["temperature_C"] = float(parameters.get("temperature_C", temp_avg))
    #parameters["feeling_temperature_C"] = float(parameters.get("feeling_temperature_C", feeling_avg))
    #parameters["humidity"] = float(parameters.get("humidity", humidity_avg))
    #parameters["windspeed"] = float(parameters.get("windspeed", windspeed_avg))

    parameters = dict(request.args)
    parameters["weathersit"] = int(parameters["weathersit"])
    parameters["date"] = dt.datetime.fromisoformat(parameters["date"])
    parameters["temperature_C"] = float(parameters["temperature_C"])
    parameters["feeling_temperature_C"] = float(parameters["feeling_temperature_C"])
    parameters["humidity"] = float(parameters["humidity"])
    parameters["windspeed"] = float(parameters["windspeed"])
    model = str(parameters["model"])

    start_prediction = dt.datetime.now()
    result = predict(parameters, model = model)
    #parameters.get('model'))
    end_prediction = dt.datetime.now() - start_prediction

    return {"result": result, "computation time": end_prediction.total_seconds()}
