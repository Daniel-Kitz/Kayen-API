import json
from csv import writer
from flask import Flask, request, jsonify
from flask.templating import render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def website():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def data_ckeck():
    if (request.method == 'GET'):
        return "Debug Message"
    if (request.method == 'POST'):

        Richtwert_Temperatur = 22.5
        Richtwert_Luftfeuchte = 280
        Richtwert_Bodenfeuchte = 12

        req = request.json
        with open('Daten/temperature.csv','a', newline='') as fd:
            writer_object= writer(fd)
            writer_object.writerow(str(req['temperature']))
            fd.close()
        with open('Daten/humidity.csv','a', newline='') as fd:
            writer_object= writer(fd)
            writer_object.writerow(str(req['humidity']))
            fd.close()
        with open('Daten/bodenfeuchte.csv','a', newline='') as fd:
            writer_object= writer(fd)
            writer_object.writerow(str(req['bodenfeuchte']))
            fd.close()

        response_liste = []
        if req['temperature'] > Richtwert_Temperatur:
            response_liste += ["Nicht Heizen"]
        else:
            response_liste += ["Heizen"]

        if req['humidity'] > Richtwert_Luftfeuchte:
            response_liste += ["Lüften"]
        else: 
            response_liste += ["Nicht Lüften"]
        if req['bodenfeuchte'] > Richtwert_Bodenfeuchte:
            response_liste += ["Nicht Bewässern"]
        else:
            response_liste += ["Bewässern"]
        

        res = {"response" : response_liste}
        return jsonify(res)


if __name__ == "__main__":
    app.run()