import pickle

import gensim
import numpy as np
import sklearn.feature_extraction as fe
from gensim.models import KeyedVectors
from scipy.sparse import hstack, csr_matrix

from expirements.pathes import path_to_data, path_to_w2v_models
from expirements.util_funcs import write_texts, write_labels

# f - 0
# m - 1

def prepare():
    texts = []
    labels = []

    with open(path_to_data + "data.tsv") as f:
        for i in f.readlines():
            s = i.replace("\n", "")
            s_split = s.split("\t")

            label = s_split[0]
            text = s_split[1]

            if label == "m":
                label = 0
            else:
                label = 1

            labels.append(label)
            texts.append(text)

    return texts, labels


texts, labels = prepare()

#texts = texts[0:10000]
#labels = labels[0:10000]

write_texts(texts)
write_labels(labels)

exit()

class SentencesIterator(object):
    def __init__(self, corpus_dir, filenames):
        self.corpus_dir = corpus_dir
        self.filenames = filenames

    def __iter__(self):
        for f in self.filenames:
            for line in open(self.corpus_dir + f):
                yield line.split()


def create_w2v_own():
    sentences = SentencesIterator(path_to_data, ["texts"])

    # update parametres
    model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)

    model.wv.save_word2vec_format(path_to_w2v_models + "/own_w2v_model", binary=True)


create_w2v_own()

def create_vectorizer(texts, use_if_idf=False):
    if use_if_idf:
        # изменить параметры
        v = fe.text.TfidfVectorizer()
    else:
        v = fe.text.CountVectorizer()

    v.fit_transform(texts)

    with open(path_to_data + "vectorizer", "wb") as f:
        pickle.dump(v, f)


create_vectorizer(texts, use_if_idf=False)

def get_vectors_by_texts_w2v_model(w2v, texts):
    arr = []

    num = 0

    # если отсутствует принимаем за zero или не учитываем?
    for i in texts:
        words = i.split(" ")
        words_exist = []
        for j in words:
            if j in w2v.vocab:
                words_exist.append(j)

        if len(words_exist) == 0:
            arr.append(np.zeros(w2v.vector_size))
        else:
            vec = w2v[words_exist]
            arr.append(np.mean(vec, axis=0))
        if num % 100000 == 0:
            print("chunk " + str(num))

        num += 1

    return np.array(arr)


def write_vec_w2v_1():
    exist_big_models = ["w2v_model_ruscorpora.bin",
                        "ruscorpora_russe.model.bin",  # 1 gb,
                        "ruwikiruscorpora_rusvectores2.bin",  # 400,
                        "ruscorpora_1_600_2.bin",  # 400,
                        "ruscorpora_1_300_10.bin"]  # 200 NOUN, ADJ

    w2v_big = KeyedVectors.load_word2vec_format(path_to_w2v_models + exist_big_models[1], binary=True)

    vec_w2v_1 = get_vectors_by_texts_w2v_model(w2v_big, texts)

    print(vec_w2v_1.shape)

    #vec_w2v_1 = np.append(vec_w2v_1, np.reshape(labels, (len(labels), 1)), axis=1)

    print(vec_w2v_1.shape)

    np.savetxt(path_to_data + "vec_w2v_1", vec_w2v_1, delimiter=',')


write_vec_w2v_1()


def write_vec_w2v_2():
    w2v_own = KeyedVectors.load_word2vec_format(path_to_w2v_models + "/own_w2v_model", binary=True)

    vec_w2v_2 = get_vectors_by_texts_w2v_model(w2v_own, texts)

    print(vec_w2v_2.shape)

    #vec_w2v_2 = np.append(vec_w2v_2, np.reshape(labels, (len(labels), 1)), axis=1)

    print(vec_w2v_2.shape)

    np.savetxt(path_to_data + "vec_w2v_2", vec_w2v_2, delimiter=',')


write_vec_w2v_2()


def write_vectorizer():
    vectorizer = pickle.load(open(path_to_data + "vectorizer", "rb"))

    vec_vectorizer = vectorizer.transform(texts)

    with open(path_to_data + "vec_vectorizer", "wb") as f:
        pickle.dump(vec_vectorizer, f)


write_vectorizer()


def data_processing():
    print("load first")
    with open(path_to_data + "vec_w2v_1", "rb") as f:
        vec_w2v_1 = np.loadtxt(path_to_data + "vec_w2v_1", delimiter=',')
    print("to csr")
    vec_w2v_1 = csr_matrix(vec_w2v_1)
    print(vec_w2v_1.shape)

    print("load second")
    with open(path_to_data + "vec_w2v_2", "rb") as f:
        vec_w2v_2 = np.loadtxt(path_to_data + "vec_w2v_2", delimiter=',')
    print("to csr")
    vec_w2v_2 = csr_matrix(vec_w2v_2)
    print(vec_w2v_2.shape)

    # print("load vectorizer")
    # with open(path_to_data + "vec_vectorizer", "rb") as f:
    #    vec_vectorizer = pickle.load(f)

    print("start hstack1")
    features = hstack((vec_w2v_1, vec_w2v_2))
    print(features.shape)

    features = features.todense()
    # print("start hstack 2")
    # features = hstack((features, vec_vectorizer))
    # print(features.shape)

    # features = features.toarray()

    np.savetxt(path_to_data + "features_full", features, delimiter=',')

data_processing()