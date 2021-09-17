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
        return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    if (request.method == 'POST'): 
        req = request.json
        if req['humidity'] >= 50:
            return "test bestanden"
        else:
            return jsonify(req)
if __name__ == "__main__":
    app.run()