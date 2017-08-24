import pickle

import numpy as np

from expirements.pathes import path_to_data


def read_vectors_csr():
    return pickle.load(open(path_to_data + "vec_vectorizer", "rb"))


def read_w2v_2(with_labels=False):
    if not(with_labels):
        path = path_to_data + "vec_w2v_2_no_label"
    else:
        path = path_to_data + "vec_w2v_2_exist_label"
    data = np.loadtxt(path, delimiter=',')
    return data


def read_w2v_1(with_labels=False):
    if not(with_labels):
        path = path_to_data + "vec_w2v_1_no_label"
    else:
        path = path_to_data + "vec_w2v_1_exist_label"
    data = np.loadtxt(path, delimiter=',')
    return data


def read_labels():
    labels = []
    with open(path_to_data + "labels") as f:
        for i in f.readlines():
            s = i.replace("\n", "")
            labels.append(s)

    return labels


def read_texts():
    texts = []

    with open(path_to_data + "texts") as f:
        for i in f.readlines():
            s = i.replace("\n", "")
            texts.append(s)

    return texts


def write_texts(texts):
    with open(path_to_data + "texts", "w") as f:
        for text in texts:
            f.write(text + "\n")


def write_labels(labels):
    with open(path_to_data + "labels", "w") as f:
        for label in labels:
            f.write(str(label) + "\n")


def read_features_full():
    data = np.loadtxt(path_to_data + "features_full", delimiter=',')
    return data

