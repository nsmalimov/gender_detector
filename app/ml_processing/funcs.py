import random
import fasttext
import os

def load_fast_text_model():
    path = os.getcwd()
    model = fasttext.load_model(path + '/expirements/model.bin', encoding='utf-8')

    return model

def get_probas(text, fasttext_model):
    res_pred = list(fasttext_model.predict_proba([text])[0][0])

    res_pred[0] = res_pred[0].replace("__label__", "")

    gender = res_pred[0]

    if gender == '0':
        proba_male = res_pred[1]
        proba_female = 1 - res_pred[1]
    else:
        proba_male = 1 - res_pred[1]
        proba_female = res_pred[1]

    proba_female = round((proba_female * 100))
    proba_male = round((proba_male * 100))

    return proba_male, proba_female
