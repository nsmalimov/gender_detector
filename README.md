Демо версия: http://54.93.235.17/

### Эксперименты
Первоночальная идея была использовать w2v embeddings на корпусе. Обучить свою w2v модель на имеющихся данных<br>

метрика: F1<br>
|Модель|counter|w2v_big|w2v_own|all w2v|tf-idf|
|----------|:-------------:|------:|------:|------:|------:|
|RF|0.549425287356|0.387592858074|0.393153526971|0.415363443013|0.525185631146|
|Log-reg|0.461463175924|0.398062066256|0.0689112029927|0.403058579575|0.460778258184|
|Bayes|0.626766545679|0.470776255708|0.485061137693|0.504651162791|0.62027112232|
|BF neural net|0|0|0|0|					


Интересно было бы посмотреть на результаты на полной конкатенации. Не тестировалось в виду сложности вычислений и необходимости применения более сложного стека.<br>

Также можно попробовать применить LSTM (https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/)<br>
CNN (https://arxiv.org/abs/1408.5882)<br>

и character level

также заменить w2v на char2vec или doc2vec.

[fasttext](https://github.com/facebookresearch/fastText)
1. [формирование эмбеддингов](https://arxiv.org/abs/1607.04606)<br>
2. [классификатор](https://arxiv.org/abs/1607.01759)<br>

### Логика работы:
Веб часть реализована с использованием Flask. Клиентская чась на Angular 1.<br>

В качестве ML части используется биндинг [python fasttexts](https://pypi.python.org/pypi/fasttext) на python.<br>

Общая вероятность считается как среднее межжду всеми предсказаниями для каждого из классов.<br>

### Установка:
#### LOCAL
```
git clone https://github.com/nsmalimov/gender_detector
cd gender_detector
pip3 install requirements.txt
python3 run.py
```
#### REMOTE
https://habrahabr.ru/post/267097/
