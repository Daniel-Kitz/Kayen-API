import json
from flask import Flask, request, jsonify
from flask.templating import render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def website():
    return render_template('index.html')

@app.route('/api/temp', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        return "Debug Message"
    if (request.method == 'POST'): 
        req = request.json
        if req['humidity'] > 40:
            return jsonify(req)
        else:
            return jsonify(req)
if __name__ == "__main__":
    app.run()