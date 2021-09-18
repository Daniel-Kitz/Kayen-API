import json
from flask import Flask, request, jsonify
from flask.templating import render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def website():
    return render_template('index.html')

@app.route('/api/temp', methods=['GET', 'POST'])
def temp():
    if (request.method == 'GET'):
        return "Debug Message"
    if (request.method == 'POST'): 
        req = request.json
        if req['temp'] > 22.5:
            return jsonify(req)
        else:
            return jsonify(req)

@app.route('/api/humidity', methods=['GET', 'POST'])
def humidity():
    if (request.method == 'GET'):
        return "Debug Message"
    if (request.method == 'POST'): 
        req = request.json
        if req['humidity'] > 280:
            return jsonify(req)
        else:
            return jsonify(req)

@app.route('/api/soil_humidity', methods=['GET', 'POST'])
def soil_humidity():
    if (request.method == 'GET'):
        return "Debug Message"
    if (request.method == 'POST'): 
        req = request.json
        if req['soil_humidity'] > 12:
            return jsonify(req)
        else:
            return jsonify(req)

if __name__ == "__main__":
    app.run()