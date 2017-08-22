import json

from flask import request
from flask import make_response
from flask.templating import render_template
from run import app

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/get_probas', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        jsonData = request.get_json()
        text = jsonData['text']

        print (text)

        # TODO
        # ml processing part

        res_dict = {"proba_male": "20", "proba_female": "80"}

        return make_response(json.dumps(res_dict))
