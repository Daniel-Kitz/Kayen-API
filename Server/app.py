import os
import json
from csv import writer, DictReader
from datetime import datetime
from flask import Flask, request, jsonify, session, redirect, url_for, flash
from flask.templating import render_template
from shutil import copy
from os import remove
import glob

# FLASK CONFIG

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["DEBUG"] = True


# INTERNAL FUNCTIONS


def currentLevel():
    level = session.get("level")
    if level == 0:
        level = 'full'
    elif level == 1:
        level = 'empty'
    return level


def internalOptions():
    with open("Daten/options.csv", "r") as file:
        currentOptions = file.read()
        currentOptions = currentOptions.split(",")
        return currentOptions

# WEBPAGE ROUTES


@app.route("/")
def home():
    return render_template("index.html", level=session.get('level', None))


@app.route("/settings")
def settings():
    return render_template("settings.html", options=options(), res='')


@app.route("/documentation")
def documentation():
    return render_template("docs.html")


@app.route("/ai")
def classification():
    return render_template("ai.html")

# API


@app.route("/api", methods=["GET", "POST"])
def data_ckeck():
    if request.method == "GET":
        return "Debug Message"
    if request.method == "POST":

        currentOptions = internalOptions()
        print(internalOptions())
        req = request.json

        print(req)
        session["level"] = req["level"]

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
        response_string = ""
        zustand_richtig = True
        if int(req["soil"]) < int(currentOptions[2]):
            response_string += "w"
            zustand_richtig = False
        if int(req["humidity"]) > int(currentOptions[1]):
            response_string += "a"
            zustand_richtig = False
        if int(req["temperature"]) < int(currentOptions[0]):
            response_string += "h"
            zustand_richtig = False
        if zustand_richtig == True:
            response_string += "r"
        response_liste += [response_string]
        res = {"response": response_liste}
        print(res)
        return jsonify(res)


@app.route("/api/options", methods=["GET", "POST"])
def options():
    if request.method == "POST":
        try:
            temp = request.form['tempInput']
            vents = request.form['ventsInput']
            water = request.form['waterInput']
            newOptions = [temp, vents, water]
            writableOptions = ''
            error = False
            with open("Daten/options.csv", "r+") as file:
                currentOptions = file.read()
                currentOptions = currentOptions.split(',')
                for i in range(len(newOptions)):
                    try:
                        if i != '':
                            int(newOptions[i])
                            currentOptions[i] = newOptions[i]
                        else:
                            error = True
                            newOptions[i] = currentOptions[i]
                    except ValueError:
                        error = True
                        newOptions[i] = currentOptions[i]
                    writableOptions += newOptions[i] + ','
                writableOptions = writableOptions.rstrip(',')
                file.seek(0)
                file.write(writableOptions)
                file.truncate()
                file.close()
                if (error):
                    flash(
                        'Caution! Some Values were blank or wrong type, so they were not saved!')
                flash('Options Saved Successfully!')
                return redirect(url_for('settings'))
        except:
            flash('')
            return redirect(url_for('settings'))
    else:
        with open("Daten/options.csv", "r") as file:
            currentOptions = file.read()
            currentOptions = currentOptions.split(",")
            return currentOptions


@app.route("/api/soil", methods=["GET"])
def get_soil():
    res = {}
    with open("Daten/soil.csv", "r") as file:
        data = file.readlines()
        for line in data:
            try:
                line = line.split(",")
                res[line[0]] = line[1].rstrip("\n")
            except IndexError:
                continue
    return jsonify(res)


@app.route("/api/temp", methods=["GET"])
def get_temp():
    res = {}
    with open("Daten/temperature.csv", "r") as file:
        data = file.readlines()
        for line in data:
            try:
                line = line.split(",")
                res[line[0]] = line[1].rstrip("\n")
            except IndexError:
                continue
    return jsonify(res)


@app.route("/api/humid", methods=["GET"])
def get_humid():
    res = {}
    with open("Daten/humidity.csv", "r") as file:
        data = file.readlines()
        for line in data:
            try:
                line = line.split(",")
                res[line[0]] = line[1].rstrip("\n")
            except IndexError:
                continue
    return jsonify(res)


@app.route("/api/level", methods=["GET"])
def get_level():
    res = {}
    res["currentlevel"] = currentLevel()
    return jsonify(res)


@app.route("/api/backupData", methods=["GET"])
def backupData():
    dataFilePath = {"temp": "Daten/temperature.csv",
                    "humid": "Daten/humidity.csv", "soil": "Daten/soil.csv"}
    now = str(datetime.now().strftime("%d-%m-%Y"))
    for item in dataFilePath.items():
        copy(item[1], f"Backup/{item[0]}_{now}")
    return jsonify(200)


@app.route("/api/resetData", methods=["GET"])
def resetData():
    dataFilePath = {"temp": "Daten/temperature.csv",
                    "humid": "Daten/humidity.csv", "soil": "Daten/soil.csv"}
    for item in dataFilePath.items():
        with open(item[1], 'r+') as file:
            file.truncate(0)
            file.close()
    return jsonify(200)


@app.route("/api/importData", methods=["GET"])
def importData():
    # * means all if need specific format then *.csv
    allFiles = glob.glob('Backup/*')
    dataFiles = glob.glob('Daten/*')

    listoflists = [[], [], []]
    newestFiles = []
    result = []
    datestamps = [[], [], []]

    for i in allFiles:
        k = i.lstrip('Backup\\').split('_')
        if (k[0] == 'humid'):
            listoflists[0] += [i]
            datestamps[0].append(datetime.strptime(k[1], '%d-%m-%Y').date())
        elif (k[0] == 'temp'):
            listoflists[1] += [i]
            datestamps[1].append(datetime.strptime(k[1], '%d-%m-%Y').date())
        else:
            listoflists[2] += [i]
            datestamps[2].append(datetime.strptime(k[1], '%d-%m-%Y').date())

    for i in datestamps:
        newestFiles.append(max(i))
    for i in range(len(newestFiles)):
        newestFiles[i] = datetime.strftime(newestFiles[i], '%d-%m-%Y')

    for i in allFiles:
        k = i.lstrip('Backup\\')
        if newestFiles[0] in i:
            result.append(i)

    print(result)

    for file in result:
        print(file)
        with open(file, 'r') as fileToRead:
            lines = fileToRead.readlines()
            print("now importing:", file)
        for i in dataFiles:
            if (file.lstrip('Backup\\').split('_')[0] in i):
                with open(i, 'r+') as fileToWrite:
                    fileToWrite.seek(0)
                    fileToWrite.writelines(lines)
                    fileToWrite.truncate()
                    fileToWrite.close()
                    print(file, "fully backed up!")
    return jsonify(200)


# FLASK DEBUG MODE
if __name__ == "__main__":
    app.run(debug=True)
