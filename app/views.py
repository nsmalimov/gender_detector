import json

from flask import make_response
from flask import request
from flask.templating import render_template
#from werkzeug.contrib.cache import SimpleCache

from app.ml_processing.funcs import get_probas, load_fast_text_model
from run import app

fasttext_model = load_fast_text_model()

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/get_probas', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        jsonData = request.get_json()
        text = jsonData['text']

        proba_male, proba_female = get_probas(text, fasttext_model)

        res_dict = {"proba_male": proba_male, "proba_female": proba_female}

        return make_response(json.dumps(res_dict))
