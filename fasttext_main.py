import fasttext
from pathes import path_to_data
from util_funcs import read_texts, read_labels
import re
from nltk.stem.snowball import SnowballStemmer

def string_preprocessing(texts):
    stemmer = SnowballStemmer("russian")

    validLetters = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for i in range(len(texts)):
        texts[i] = texts[i].lower()

        s = ""
        for char in texts[i]:
            if char in validLetters or char == ' ':
                s += char

        texts[i] = s.replace("  ", " ")

        l = [stemmer.stem(word) for word in texts[i].split(" ")]

        texts[i] = " ".join(l)

        if i % 1000 == 0:
            print (i)

    return texts

def update_text_for_fasttext():
    texts = read_texts()

    labels = read_labels()

    num_sep = len(texts) / 100 * 80
    num_sep = int(num_sep)


    num = 0
    with open(path_to_data + "texts_updated_train", "w") as f:
        for i in texts:
            f.write("__label__" + labels[num] + " " + i.lower() + "\n")
            num += 1

            if num_sep == num:
                break

    num = 0
    with open(path_to_data + "texts_updated_test", "w") as f:
        for i in texts:
            if num > num_sep:
                f.write("__label__" + labels[num] + " " + i.lower() + "\n")

            num += 1

            #if num_sep == num:
            #    break

    #exit()
update_text_for_fasttext()

#print (dir(fasttext))
#exit()
# Skipgram model
#model = fasttext.skipgram(path_to_data + "texts", 'model')

classifier = fasttext.supervised(path_to_data + "texts_updated_test", 'model', label_prefix='__label__',
                                 epoch=30)

result = classifier.test(path_to_data + "texts_updated_test")
print ('P@1:', result.precision)
print ('R@1:', result.recall)
print ('Number of examples:', result.nexamples)

# >> cat cooking.stackexchange.txt | sed -e "s/([.!?,'/()])/ 1 /g" | tr "[:upper:]" "[:lower:]" > cooking.preprocessed.txt

#print (model.words) # list of words in dictionary

# CBOW model
#model = fasttext.cbow('data.txt', 'model')
#print model.words # list of words in dictionary