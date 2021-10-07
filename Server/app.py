import json
from csv import writer, DictReader
from datetime import datetime
from flask import Flask, request, jsonify
from flask.templating import render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home():
    return "hi"


@app.route("/api", methods=["GET", "POST"])
def data_ckeck():
    if request.method == "GET":
        return "Debug Message"
    if request.method == "POST":

        Richtwert_Temperatur = 22.5
        Richtwert_Luftfeuchte = 280
        Richtwert_Bodenfeuchte = 12

        req = request.json

        now = str(datetime.now().strftime("%d-%m-%Y- %H:%M"))

        with open("Daten/temperature.csv", "a", newline="") as fd:
            writer_object = writer(fd)
            writer_object.writerow([now, str(req["temperature"])])
            fd.close()
        with open("Daten/humidity.csv", "a", newline="") as fd:
            writer_object = writer(fd)
            writer_object.writerow([now, str(req["humidity"])])
            fd.close()
        with open("Daten/soil.csv", "a", newline="") as fd:
            writer_object = writer(fd)
            writer_object.writerow([now, str(req["soil"])])
            fd.close()

        response_liste = []
        if req["soil"] < Richtwert_Bodenfeuchte:
            response_liste += ["w"]
        if req["humidity"] > Richtwert_Luftfeuchte:
            response_liste += ["a"]
        if req["temperature"] < Richtwert_Temperatur:
            response_liste += ["h"]

        res = {"response": response_liste}
        return jsonify(res)


@app.route("/api/soil", methods=["GET"])
def get_soil():
    res = {}
    with open("Daten/soil.csv", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.split(",")
            res[line[0]] = line[1].rstrip("\n")
    return jsonify(res)


@app.route("/api/temp", methods=["GET"])
def get_temp():
    res = {}
    with open("Daten/temperature.csv", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.split(",")
            res[line[0]] = line[1].rstrip("\n")
    return jsonify(res)


@app.route("/api/humid", methods=["GET"])
def get_humid():
    res = {}
    with open("Daten/humidity.csv", "r") as file:
        data = file.readlines()
        for line in data:
            line = line.split(",")
            res[line[0]] = line[1].rstrip("\n")
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
