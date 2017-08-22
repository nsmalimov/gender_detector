import keras
import numpy as np
from keras import metrics
from keras.layers import Dense, Dropout, Embedding, Activation
from keras.models import Sequential
from scipy.sparse import csr_matrix

import tensorflow as tf

from sklearn.model_selection import train_test_split

from util_funcs import read_vectors_csr, read_labels, read_w2v_1, read_w2v_2

#batch_size = 32
#nb_epoch = 5

def generate_arrays_from_file(path):
    num = 0
    arr_x = None
    arr_y = []

    while 1:
        f = open(path)
        for line in f:
            line = line.replace("\n", "")
            line_split = line.split(",")

            x = np.array(line_split[0:-1])
            #x = [float(i) for i in x]

            x = x.astype(float)

            y = int(float(line_split[-1]))

            if arr_x is None:
                arr_x = np.array([x])
            else:
                arr_x = np.append(arr_x, [x], axis=0)

            arr_y.append(int(y))

            if num % 1000 == 0:
                print (num)

            if (num % 10000 == 0 and num != 0):
                num += 1
                print (len(arr_x), len(arr_y))
                yield (np.array(arr_x), arr_y)

            num += 1

        f.close()

def keras_perceptron_plain(X, y):

    tf.reset_default_graph()
    sess = tf.InteractiveSession()

    model = Sequential()
    # среднее между размером входа и размером выхода
    model.add(Dense(32, activation='relu', input_dim=100))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # model.fit_generator(generator=nn_batch_generator(X, y, 32),
    #                     nb_epoch=nb_epoch,
    #                     samples_per_epoch=X_train.shape[0])

    #model.fit_generator(generate_arrays_from_file('/home/nur/PycharmProjects/gender_detector/data/vec_w2v_2'),
    #                    steps_per_epoch=3, workers=1)

    model.fit(X, y, epochs=30, batch_size=32)

    #PFTExtractingFs(model_id).save_keras_perceptron(model, "neural")

    return model

features = read_w2v_2(False)
labels = read_labels()

print ("start train")
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.33, random_state=42)

keras_perceptron_plain(X_train, y_train)


