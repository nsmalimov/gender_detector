import random

def get_probas(text):
    proba_male = random.uniform(0, 1)

    proba_female = 1 - proba_male

    proba_female = round((proba_female * 100))
    proba_male = (round((proba_male * 100)))

    return proba_male, proba_female
